# from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from blog.models import Post, Category, Tag

class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_queryset(self):
        return Post.objects.all().select_related('category').prefetch_related('tags', 'comment_set')

    def get_context_data(self, **kwargs):
        pass