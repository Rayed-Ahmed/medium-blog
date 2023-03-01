from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
import uuid

from App_Blog.models import Blog, Comment, Likes

# Create your views here.

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        encoded = title.replace(' ', '-') + '-' + str(uuid.uuid4())
        blog_obj.slug = slugify(encoded)
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'App_Blog/blog_details.html', context={'blog': blog})