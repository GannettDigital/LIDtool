from django.urls import path
from lid.views import *
from django.views.generic import TemplateView
from django.conf.urls import *

urlpatterns = [
    path('add/', AddModel),
    path('top-secret/', SecretAddModel),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('thanks/', TemplateView.as_view(template_name="thanks.html")),
#    path('<state>/<billno>/<year1>', MatchDetailView.as_view(), name='match-detail'),
    path('search/', NatlSearch),
    path('<statename>/search/', Search),
    path('<statename>/<bill>/<year>/<modelid>', SimListView.as_view(), name='match-detail'),
    path('<statename>/export', CsvExport),
    path('<state>/', MatchList.as_view()),
    path('', Main.as_view(template_name="lid/main.html")),    
]
