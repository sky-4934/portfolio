from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html',{'blog':blog})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)  #pk means primary key
    return render(request, 'blog/detail.html',{'detailblog':detailblog})
