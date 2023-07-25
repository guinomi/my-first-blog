from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

#from django.http import HttpResponse
#from .forms import InputForm



#import settings
from django.conf import settings
from django.core.mail import send_mail



import requests
import json

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  
    return render(request, 'blog/post_list.html', {'posts': posts})

boo = [False]*200
def post_detail(request, pk):
    Post.objects.get(pk=pk)
    
    post = get_object_or_404(Post, pk=pk)
    

    #pkはブログの回数で一回だけ通知が来るようにしたい
    
    if boo[pk]==False:

        #スマホに通知がいくようにする
        #ヘッダーとCookieとJSONパラメータを作成
        headers = {"Content-Type": "application/json"}
        cookies = {"test_cookie": "aaa"}
        data = json.dumps({"test": "hoge"})

        #POSTリクエストを送信
        response = requests.post("https://maker.ifttt.com/trigger/hello/with/key/bmJJC2vwlzldgPEhoZmrk3", headers=headers, cookies=cookies, data=data)

        '''
        #gmailに送る
        subject = 'hello'
        message = "誰か来たのでアプリ開いてみましょう！！"
        from_email = ''
        recipient_list = ['g20904em@gm.tsuda.ac.jp']
        #print('mail is' + settings.EMAIL_HOST_USER )
        #print(send_mail(subject, message, from_email, recipient_list,fail_silently=False,))
        #この返り値が１になればOK
        send_mail(subject,message, from_email,recipient_list,fail_silently=False,)
        '''
        boo[pk] = True

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








