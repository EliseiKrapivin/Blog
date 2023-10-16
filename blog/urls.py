from django.urls import path
from . import views
from .views import PostListView
from .views import PostDetailView
from .views import PostCreateView
from .views import PostUpdateView
from .views import PostDraftListView
from .views import PostPublishView
from .views import PostRemoveView

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),

    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    #path('post/new/', views.post_new, name='post_new'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),

    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),

    #path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('drafts/', PostDraftListView.as_view(), name='post_draft_list'),

    #path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/publish/<int:pk>/', PostPublishView.as_view(), name='post_publish'),

    #path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/remove/<int:pk>/', PostRemoveView.as_view(), name='post_remove'),
]