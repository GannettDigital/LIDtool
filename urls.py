from django.urls import path
from lid.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('<state>/<pk>/', MatchDetailView.as_view(), name='match-detail'),
    path('<state>/', MatchList.as_view()),
    path('', Main.as_view(template_name="lid/main.html")),    
]
