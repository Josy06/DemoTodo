from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Task
from .froms import todofrom


# This is class generic views
# genric veiws has alredy fetched datas
class tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'


class taskdetails(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


def open(request):
    task1 = Task.objects.all()  # this will display the details at the same page.
    if request.method == 'POST':  # this fetch the data
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'index.html', {'task1': task1})


# def details(request): This is the function for that
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task1 = Task.objects.get(id=id)
    form1 = todofrom(request.POST or None, instance=task1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form1, 'task1': task1})


def detail(request):
    return render(request, 'details.html')
