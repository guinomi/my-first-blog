from django.urls import path
from . import views


urlpatterns = [
    #リストをホストにする
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #newのところをcustomerにする
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.index, name = 'index'),
    path('confirm',views.confirm,name='confirm'),
    path('regist', views.regist, name='regist'),
]