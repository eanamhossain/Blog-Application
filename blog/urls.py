from django.urls import path
# from blog.views import home, post_list , post_detail, post_create, post_update, post_delete
from blog.views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
app_name = 'blog'



urlpatterns = [
    path('',PostListView.as_view(), name='post_list'),
    path('post-detail/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post-create/',PostCreateView.as_view(), name='post_create'),
    path('post-update/<int:pk>/',PostUpdateView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/',PostDeleteView.as_view(), name='post_delete'),

]
