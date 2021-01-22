from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.category, name='category'),
    path('<int:category_id>/', views.index, name='index'),
    path('<int:category_id>/<int:question_id>/', views.detail, name='detail'),
    path('<int:category_id>/<int:question_id>/results/', views.results, name='results'),
    path('<int:category_id>/<int:question_id>/vote/', views.vote, name='vote'),
]


# urlpatterns = [
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     # Add path calls for new views!
#     # detail() method will run and display whatever ID you provide in URL
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
