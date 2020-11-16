from os.path import altsep, relpath

from django.conf.urls import url
from django.http import request,HttpResponse
from django.shortcuts import redirect, render

# from .models import Student
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Post
from .forms import PostForm,UserUpdateForm,UpdateProfileForm
# from .forms import UserRegisterForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
   # std = Student.objects.all() 
    return render(request,'home.html',{'posts':posts})

def profile(request):
    return render(request, 'home.html')

# def signup(request):
#     form = UserRegisterForm()
#     if request.method =="POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     context ={'fm':form}
#     return render(request,'b.html',context)   

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']

        if password!=password2: 
            messages.warning(request,'password does not match')
            return redirect('signup')
        
        elif len(username)<5:
            messages.warning(request,'username weak')
            return redirect('signup')


        elif User.objects.filter(username=username).exists(): 
             messages.warning(request, 'Username is already taken')
             return redirect('signup')  

        elif User.objects.filter(email=email).exists():
             messages.warning(request,'email-id is already exist')
             return redirect('signup')

        else:    
            x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            x.save()
            messages.success(request,'signup successfully')
        
        print("user created")
        return redirect('login')


    else:
         return render(request,'b.html')





def login(request):
    if request.method=="POST":
        username1=request.POST['username']
        password1=request.POST['password']
        user = auth.authenticate(
            username=username1, password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
              
        else:
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def dashboard(request):
    current_user = request.user
    posts = Post.objects.filter(author=current_user)
    context ={'posts':posts}
    return render(request,'dashboard.html',context)


def add_post(request):
        post_form = PostForm()
        if request.method == 'POST':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                user_post = post_form.save(commit=False)
                user_post.author = request.user
                user_post.save()
                return redirect('home')
            
       
           
        return render(request,'addpost.html',{'p_form':post_form})

def profile_settings(request):
    fm = UserUpdateForm(instance=request.user)
    p_form=UpdateProfileForm(instance=request.user.profile)

    if request.method=='POST':
        fm = UserUpdateForm(request.POST,instance=request.user)
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if fm.is_valid() and p_form.is_valid():
            fm.save()
            p_form.save()
            return redirect('profile-settings')

    context={'fm':fm,'pform':p_form}
    return render(request,'profile-settings.html',context)

def update_post(request, id):
    pos = Post.objects.get(id=id)
    fm =PostForm(instance=pos)

    if request.method=="POST": 
        fm = PostForm(request.POST,instance=pos)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    context={'p_form':fm}
    return render(request,'addpost.html',context)

def delete_post(request, id):
    pos = PostForm.objects.get(id)
    pos.delete()
    return redirect('home')
    
    
        


