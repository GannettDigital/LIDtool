from django.urls import path
from lid.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html")),
#    path('<state>/<billno>/<year1>', MatchDetailView.as_view(), name='match-detail'),
    path('<statename>/<bill>/<year>/<modelid>', SimListView.as_view(), name='match-detail'),
    path('<state>/', MatchList.as_view()),
    path('', Main.as_view(template_name="lid/main.html")),    
]
