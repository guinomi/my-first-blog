from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

from django.http import HttpResponse
from .forms import InputForm



from django.conf import settings 
import datetime  
from django.core.mail import send_mail


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(request.POST,instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})







def index(request):
    params = {
        'input_form' : InputForm()
    }
    return render(request, 'blog/input.html', params)

def confirm(request):
    input_form = InputForm(request.POST)

    if input_form.is_valid():
        params = {'input_form':input_form,'lbl_checked':'確認済'
        }
        return render(request,'blog/confirm.html',params)
    else:
        params={
            'input_form' : input_form
        }
        return render(request, 'blog/input.html', params)
    
def regist(request):
    if "send" in request.POST:
        return render(request,'blog/complete.html')
    elif "back" in request.POST:
        input_form = InputForm(request.POST)
        params = {
            'input_form':input_form
        }
        return render(request, 'blog/input.html',params)



