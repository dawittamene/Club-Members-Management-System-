from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,AddMembersModelForm,PostNewsModelForm,ApplicantModelForm
from .decorators import unauthenticated_user,allowed_users,admin_only



def index(request):
    return render(request, 'base/index.html')
def UserRegisterForm(request):
    form=ApplicantModelForm()
    if request.method == 'POST':
        form=ApplicantModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apply successfully!!! ')
            return redirect('newsuserview')
        
    
    return render(request, 'base/userform.html')

def main(request):
    return render(request, 'base/main.html')
@admin_only
def adminpage(request):
   
    addmembers = Members.objects.all()
    total_members=addmembers.count()
    dev=addmembers.filter(division='dev').count()
    cpd=addmembers.filter(division='cpd').count()
    cbd=addmembers.filter(division='cbd').count()
    
    
    
    context = {'addmembers':addmembers,'total_members':total_members,'dev':dev,'cpd':cpd,'cbd':cbd}
    return render(request, 'admin/adminpage.html',context)
def NewsPost(request):
    form=PostNewsModelForm()
    if request.method == 'POST':
        form=PostNewsModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text created successfully!!! ')
            return redirect('adminpage')
    return render(request, 'admin/newspostpage.html')
def NewsUserView(request):
    postnews = PostNews.objects.all()

    return render(request, 'base/news.html',{'postnews':postnews})
@admin_only
def AddMembers(request):
    form=AddMembersModelForm()
    if request.method == 'POST':
        form=AddMembersModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created successfully!!! ')
            return redirect('adminpage')
            
    return render(request, 'admin/addmembers.html')
    
    
def Profile(request):
    return render(request, 'base/Profile.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.success(request, "username or password is incorrect")
    context ={}
    return render(request, 'base/login.html', context)


def signuppage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account created successfully for ' + user)
            return redirect('loginpage')
        
    context ={'form':form}
    return render(request, 'base/signup.html', context)
def logoutPage(request):
    logout(request)
    return redirect('loginpage')
          
def view_profile(request, id):
    member = Members.objects.get(id=id)
    if request.method == 'POST':
        member.firstname = request.POST['firstname']
        member.lastname = request.POST['lastname']
        member.email = request.POST['email']
        member.division = request.POST['division']
        member.phonenumber = request.POST['phonenumber']
        member.save()
        messages.success(request, 'account Saved successfully!!! ')
    return render(request, 'admin/edit.html', context={"member": member})

def updateprofile(request, id):
    profile = User.objects.get(id=id)
    return render(request, 'base/updateprofile.html', {'profile':profile})