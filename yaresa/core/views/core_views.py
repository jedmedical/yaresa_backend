from core.forms.core_forms import NewUserForm
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request,'dashboard.html')

def add_new_user(request):

    if request.method == "POST":
        new_user_form = NewUserForm(request.POST)
        if new_user_form.is_valid():
            pass
            
    new_user_form = NewUserForm()
    context = {'new_user_form':new_user_form}
    return render(request,'add_new_user.html',context)