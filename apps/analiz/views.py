from django.shortcuts import render, redirect
from .models import Task, Category
from .forms import TaskForm
from django.core.paginator import Paginator

def task_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        tasks = Task.objects.filter(category_id=category_id).order_by('created_at')
    else:
        tasks = Task.objects.all().order_by('created_at')
    
    categories = Category.objects.all()

    paginator = Paginator(tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'analiz/task_list.html', {'task':page_obj, 'categories':categories})

def task_add(requests):
    if requests.method == 'POST':
        form = TaskForm(requests.POST)
        if form.is_valid():
            form.save()
            print("Task added successfully!")
            return redirect('task_list')
    else:
        form = TaskForm
    Categories = Category.objects.all()
    return render(requests, 'analiz/task_form.html', {'form':form, 'categories' : Categories})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'analiz/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'analiz/task_confirm_delete.html', {'task': task})
