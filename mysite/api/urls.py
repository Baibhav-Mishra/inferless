from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('task-overview/', views.apiOverview),
    path('task/', views.task),
    path('task/<str:pk>/', views.task_pk),
]