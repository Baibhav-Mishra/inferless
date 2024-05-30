from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('task-overview/', views.apiOverview),

    path('task-create/', views.taskCreate),
    path('task-list/', views.taskList),
    path('task-read<str:pk>/', views.get_param),

    path('task-update/<str:pk>/', views.taskUpdate),
    path('task-delete/<str:pk>/', views.taskDelete),








]