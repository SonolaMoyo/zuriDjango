from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog.post_list"


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog.post_form"
    success_url = reverse_lazy("blog:all")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog.post_detail"


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    template_name = "blog.post_form"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = "blog.post_confirm_delete"
    success_url = reverse_lazy("blog:all")