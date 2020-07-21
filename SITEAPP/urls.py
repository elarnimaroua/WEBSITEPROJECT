from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    path('marrakech', views.marrakech, name='marrakech'),
    path('marrakech/monuments', views.monumentmarrakech, name='monumentmarrakech'),
    path('marrakech/restaurants', views.restaurantmarrakech, name='restaurantmarrakech'),
    path('marrakech/hotels', views.hotelmarrakech, name='hotelmarrakech'),
    path('marrakech/activites', views.activitemarrakech, name='activitemarrakech'),
    path('posts', PostListView.as_view(), name='posts'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
