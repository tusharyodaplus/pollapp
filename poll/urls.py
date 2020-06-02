from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    # ex: /polls/
    path('poll/', views.index, name='index'),
    # ex: /polls/5/
    path('poll/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('poll/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('poll/<int:question_id>/vote/', views.vote, name='vote'),
]