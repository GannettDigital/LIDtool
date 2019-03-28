from django.utils import timezone
from django.views.generic.detail import DetailView
from lid.models import *
from bakery.views import BuildableDetailView, BuildableListView
from django.shortcuts import *
from django.db.models import *
from django.http import HttpResponse
from lid.forms import *
import csv

def NatlSearch(request):
    query = request.GET.get('q', '')
    exploded = query.split(" ")
    q_objects = Q()
    for term in exploded:
        q_objects |= Q(modelsubject__icontains=term)|Q(billtitle__icontains=term)|Q(modelcat__icontains=term)|Q(modeldesc__icontains=term)

    if query:
        qset = (
            q_objects
        )
        results = Match.objects.filter(qset).filter(lidscore__gt=80).values("state", "modelid", "billno", "timestamp", "year1", "modeldesc", "modelcat", "primarysponsors").distinct()


    else:
        results = []

    dictionaries = {'results': results, 'query': query,}
    return render(request, 'lid/natlsearch.html', dictionaries)


def Search(request, statename):
    query = request.GET.get('q', '')
    exploded = query.split(" ")
    q_objects = Q()
    for term in exploded:
        q_objects |= Q(modelsubject__icontains=term)|Q(billtitle__icontains=term)|Q(modelcat__icontains=term)|Q(modeldesc__icontains=term)


    if query:
        qset = (
            q_objects
        )
        results = Match.objects.filter(state=statename).filter(lidscore__gt=80).filter(qset).values("state", "modelid", "billno", "timestamp", "year1", "modeldesc", "modelcat", "primarysponsors").distinct()
        
    else:
        results = []

    dictionaries = {'state': statename, 'results': results, 'query': query,}
    return render(request, 'lid/search.html', dictionaries)


def AddModel(request):
    if request.method == 'POST':
        form = ModelSuggestionForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
        return HttpResponseRedirect('/lid/thanks')
    else:
        form = ModelSuggestionForm()
    return render(request, 'lid/addmodel.html', {'form': form,})

#This is a secret view, at /lid/top-secret, that lets us add a sanitized model to the app
def SecretAddModel(request):
    if request.method == 'POST':
        form = ModelAddingForm(request.POST)
        if form.is_valid():
            body = { 
              "api_key": "143d1680acbecad3c3abf74b3dbfacc2", 
               "model_text_id": 0, 
               "model_type_id": form.cleaned_data['model_type_id'], 
               "category_id": form.cleaned_data['category_id'], 
               "subject_id": form.cleaned_data['subject_id'], 
               "description_id": form.cleaned_data['description_id'], 
               "model_name": str(form.cleaned_data['model_name']), 
               "source_link": str(form.cleaned_data['source_link']), 
               "model_legislation_source": str(form.cleaned_data['model_legislation_source']), 
               "model_legislation_text": str(form.cleaned_data['model_legislation_text'])
             }
        myurl = "https://statehouses-api.gannettdigital.com/api/v1.0/UpdateModelText"
        req = urllib.request.Request(myurl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)

        return HttpResponseRedirect('/lid')
    else:
        form = ModelAddingForm()
    return render(request, 'lid/secretaddmodel.html', {'form': form,})



class SimListView(BuildableListView):
    context_object_name = 'sim_list'
    template_name = 'lid/match_detail2.html'
    def get_queryset(self):
        return Match.objects.filter(state=self.kwargs['statename'], billno=self.kwargs['bill'], year1=self.kwargs['year'], modelid=self.kwargs['modelid'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = self.kwargs['statename']
        context['match'] = Match.objects.filter(state=self.kwargs['statename'], billno=self.kwargs['bill'], year1=self.kwargs['year'], modelid=self.kwargs['modelid']).order_by('-id')[0]
        context['other_matches'] = Match.objects.filter(lidscore__gte=80).filter(modelid=self.kwargs['modelid']).distinct('state')
        try:
            context['model_deets'] = ModelText.objects.get(model_id=self.kwargs['modelid'])
        except:
            context['model_deets'] = []
        return context

class Main(BuildableListView):
    context_object_name = 'state_list'
    def get_queryset(self):
        return Match.objects.filter(lidscore__gte=80).values('state').exclude(state='US').annotate(statecount=Count('state')).order_by('state')

class MatchList(BuildableListView):
    context_object_name = 'match_list'
    def get_queryset(self):
        return Match.objects.filter(state=self.kwargs['state']).filter(lidscore__gte=80).values("modelid", "billno", "timestamp", "year1", "billtitle", "modelcat", "primarysponsors").distinct().order_by('-year1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = self.kwargs['state']
        modelids = Match.objects.filter(state=self.kwargs['state']).filter(lidscore__gte=80).values('modelid').distinct()
        context['top_sources'] = ModelText.objects.filter(model_id__in=modelids).values('model_source').annotate(ccount=Count('model_source')).order_by('-ccount') [:3]
        context['top_stooges'] = Match.objects.filter(state=self.kwargs['state']).filter(lidscore__gte=80).exclude(primarysponsors="").values('primarysponsors').annotate(scount=Count('primarysponsors')).order_by('-scount')[:3]
        context['top_topics'] = Match.objects.filter(state=self.kwargs['state']).filter(lidscore__gte=80).values('modelsubject').annotate(scount=Count('modelsubject')).order_by('-scount')[:3]
        return context

def CsvExport(request, statename):
    matches = Match.objects.filter(state=statename).filter(lidscore__gte=80).values("modelid", "billno", "year1", "billtitle", "modelcat", "primarysponsors", "cosponsors", "othersponsors").distinct()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="LIDexport.csv"'
    writer = csv.writer(response)
    writer.writerow(['billno','year','primarysponsors','cosponsors','othersponsors','modelcat','modelid'])
    for row in matches:
        writer.writerow([row['billno'], row['year1'], row['primarysponsors'], row['cosponsors'], row['othersponsors'], row['modelcat'], row['modelid']])
    return response
