from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoItem
from .forms import AddlistForm,SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# home page
# @login_required(login_url='login')
def home_todo(request):
    todo = TodoItem.objects.all()
    return render(request, 'index.html',{'todo':todo})

# add todo_list
@login_required(login_url='login')
def add_todo(request):
    form = AddlistForm()
    if request.method == 'POST':
        form = AddlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = AddlistForm()
    return render(request,'add_todo.html', {'form':form})
        
# update_list
def update_todo(request,id):
    todo = TodoItem.objects.get(pk=id)
    form = AddlistForm(instance=todo)
    if request.method == 'POST':
        form = AddlistForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'add_todo.html',context)
    
# delete todo_list
def delete_todo(request,id):
    todo = get_object_or_404(TodoItem, pk=id)
    todo.delete()
    return redirect('home')




# signup form
def user_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = SignUpForm()
    return render(request,'signup.html',{'form':form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('/login/')