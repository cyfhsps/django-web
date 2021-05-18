from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    content={
    'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',content)#key of content can be accessed in html file through render function

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'#<app>/<model>_<view>.html
    context_object_name='posts'
    ordering = ['-date_posted']
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/home.html'#<app>/<model>_<view>.html
    context_object_name='posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields =['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model =Post
    fields =['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    


def about(request):
        return render(request,'blog/about.html')

