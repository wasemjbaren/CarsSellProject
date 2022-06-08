from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from .models import *




def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'GET':
            return render(request,'login.html')
        elif request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                print('wrong username or password')
                return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('login')






@method_decorator(login_required(login_url='login'),name='dispatch')
class Profile(ListView):
    model = Post
    template_name = "profile.html"
    paginate_by = 8


    def get_queryset(self):
        return Post.objects.filter(user = self.request.user).order_by('-date_created')




class SignupView(CreateView):
    model = User
    form_class =SignupForm
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('profile')
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        
        return super(SignupView, self).get(*args,**kwargs)



@method_decorator(login_required(login_url='login'),name='dispatch')
class AccountSettingsView(UpdateView):
    model = User                        #profile_pic named in model
    fields = ['first_name','last_name','phone_number','country']
    template_name = 'account_settings.html'
    success_url = '/profile/'
    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(login_required(login_url='login'),name='dispatch')
class CreatePost(CreateView):
    model = Post
    fields =['car_type','car_model','car_year','car_yad','car_price','car_pic']
    template_name = "new_post.html"
    success_url = '/profile/'

    #sa7eb alpost:
    def form_valid(self, form):
        #logged in user
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)



@method_decorator(login_required(login_url='login'),name='dispatch')
class SearchResults(ListView):
    model = Post
    template_name = "search-results.html"

    def get_queryset(self):
        post_car_type = self.request.GET['search-type']
        post_car_model =self.request.GET['search-model']
        post_car_year =self.request.GET['search-year']
        post_car_price =self.request.GET['search-price']

        qs = Post.objects.filter(car_type__contains=post_car_type,car_model__contains=post_car_model,car_year__contains=post_car_year,car_price__contains=post_car_price)
        return qs



@method_decorator(login_required(login_url='login'),name='dispatch')
class Home(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.all()
