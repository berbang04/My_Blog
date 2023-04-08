from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import (ListView)

class home_view(ListView):
    model = Post
    template_name = 'clean_blog/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    
    paginate_by = 1
# def home_view(request):
#     post=Post.objects.all()
#     paginator=Paginator(post,1)
#     page_number = request.GET.get('page')
#     posts = paginator.get_page(page_number)
#     context=dict(
#         posts=posts,

#     )
    # return render(request,'clean_blog/index.html',context)
def about_view(request):
    context=dict()
    return render(request,'clean_blog/about.html',context)
def contact_view(request):
    context=dict()
    return render(request,'clean_blog/contact.html',context)
def post_view(request,pk):
    posts=Post.objects.filter(pk=pk)
    context=dict(
       posts=posts
       

       
    )
    return render(request,'clean_blog/post.html',context)

# Create your views here.
