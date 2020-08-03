from django.shortcuts import render
from . models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Post
    success_url = '/'  #to redirect to the specific url after succesfully deletion
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    success_url = '/'  #to redirect to the specific url after succesfully creation

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

#To add an author to the initial model entity 
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

#To make sure that the person going to update is loggedIn person
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'}) 