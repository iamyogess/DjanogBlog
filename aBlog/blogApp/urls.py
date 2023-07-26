from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('add_post/', views.AddPostView, name='add_blog_post'),
    path('update/<int:id>', views.UpdatePostView, name='update_blog_post'),
    path('delete<int:id>', views.DeletePostView, name='delete_blog_post'),
    path('blog_details/', views.BlogDetailsView, name='blog_details'),
]
