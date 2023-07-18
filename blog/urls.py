from django.urls import path
from . import views


urlpatterns = [
    #リストをホストにする
    path('post/list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #post_newのところをcustomerにする
    path('', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]