from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from blog.models import Post
from blog.forms import PostUpdateForm, PostFrom
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy



class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'  


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostFrom
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostFrom
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        post_obj = self.get_object()
        if self.request.user == post_obj.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post_obj = self.get_object()
        if self.request.user == post_obj.author:
            return True
        return False
        