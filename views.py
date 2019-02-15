from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from lid.models import Match
from bakery.views import BuildableDetailView, BuildableListView
from django.db.models import Count

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
        return context

class Main(BuildableListView):
    context_object_name = 'state_list'
    def get_queryset(self):
        return Match.objects.filter(lidscore__gte=80).values('state').exclude(state='US').annotate(statecount=Count('state')).order_by('state')

class MatchList(BuildableListView):
    context_object_name = 'match_list'
    def get_queryset(self):
        return Match.objects.filter(state=self.kwargs['state']).filter(lidscore__gte=80).values("modelid", "billno", "timestamp", "year1", "modeldesc", "modelcat", "primarysponsors").distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = self.kwargs['state']
        context['top_stooges'] = Match.objects.filter(state=self.kwargs['state']).filter(lidscore__gte=80).exclude(primarysponsors="").values('primarysponsors').annotate(scount=Count('primarysponsors')).order_by('-scount')[:3]
        context['top_sources'] = Match.objects.filter(state=self.kwargs['state']).filter(lidscore__gte=80).values('modeltype').annotate(scount=Count('modeltype')).order_by('-scount')
        return context
