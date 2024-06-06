from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from .const import *
def say_hello(request):
    return render(request, 'hello.html',{'name': 'Baibhav'})


# @api_view([GET])
# def d_page(request):
#     return render(request, 'addition.html')

# @api_view([GET])
# def add_num(request):
#     val1 =  int(request.GET["num1"])
#     val2 =  int(request.GET["num2"])
#     val3 = val1+val2
#     r = {"result": val3}
#     return Response(r)

@api_view([GET])
def api_overview(request):
    api_urls = {
        'Overview': '/task-overview/',
        'Create': '/task-create/',
        'Read': '/task-read/<str:pk>',
        'List': '/task-list/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>'
    }
    return Response(api_urls)


# @api_view([GET])
def task_read(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


# @api_view([GET])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

def task_create(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

def task_update(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# @api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully deleted")

@api_view([GET, DELETE, POST])
def task_pk(request, pk):
    if request.method == GET: 
         return task_read(request, pk)
    elif request.method == POST:
         return task_update(request, pk)
    elif request.method == DELETE:
         return task_delete(request, pk)
         

@api_view([GET, POST])
def task(request):
    if request.method == GET: 
         return taskList(request)
    elif request.method == POST:
         return task_create(request)
   


