from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserForm
from .models import UserModel


# Create your views here.


def create(request):
    form = UserForm()
    # print(request.POST)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created')
            return redirect('read')
    context = {'form': form}
    return render(request, 'crud_app/create.html', context)


def read(request):
    user_data = UserModel.objects.all()
    context = {'user_data': user_data}
    return render(request, 'crud_app/read.html',context)


def update(request, pk):
    get_user_data = get_object_or_404(UserModel,pk=pk)
    form = UserForm(instance=get_user_data)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Updated')
            return redirect('read')
    context = {'form': form}
    return render(request, 'crud_app/update.html',context)


def delete(request, pk):
    get_user = get_object_or_404(UserModel, pk=pk)
    get_user.delete()
    messages.success(request, 'User Deleted')
    return redirect('/')