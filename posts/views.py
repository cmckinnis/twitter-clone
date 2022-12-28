from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
 
# Create your views here.
# def base(request):
#     return render(request, 'base.html')

# def posts(request):
#     return render(request, 'posts.html')

def index(request):
   # If the method is POST
   if request.method == 'POST':
       form = PostForm(request.POST, request.FILES)
       # IF the form is valid
       if form.is_valid():
           # Yes, save
           form.save()
           # Redirect to Home
           return HttpResponseRedirect('/')
       else:
           #IF No- show error
           return HttpResponseRedirect(form.errors.as_json())
      
   # Get all posts, limit = 20
   posts = Post.objects.all().order_by('-created_at')[:20]
  
   #show
   return render(request, 'posts.html',
                 {'posts': posts})
  
def delete(request, tweet_id):
   # Find post
   post = Post.objects.get(id=tweet_id)
   post.delete()
   return HttpResponseRedirect('/')


def like(request, tweet_id):
    post = Post.objects.get(id=tweet_id)
    post.like += 1
    post.save()
    return HttpResponseRedirect('/')


def edit(request, tweet_id):
    post = Post.objects.get(id=tweet_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    form = PostForm()
    return render(request, 'edit.html', {'post':post, 'form':form})