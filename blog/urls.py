from django.urls import path
from . import views


#http://127.0.0.1:8000           =>  index
#http://127.0.0.1:8000/index     =>  index
#http://127.0.0.1:8000/blogs     =>  blogs
#http://127.0.0.1:8000/blogs/5   =>  blogs-detail


urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='index'),
    path("blogs", views.blogs, name='blogs'),
    path("blogs/<int:id>", views.blog_details, name='blog_details'),
]