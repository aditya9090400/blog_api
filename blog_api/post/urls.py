from django.urls import path
from .views import (PostListView,
				    PostDetailView,
				    PostUpdateView,
				    PostDeleteView,
				    PostCreateView,
				    )

urlpatterns = [
	path("", PostListView.as_view(), name="post_list"),
	path("create", PostCreateView.as_view(), name="post_create"),
	path("<str:slug>", PostDetailView.as_view(), name="post_detail"),
	path("update/<str:pk>", PostUpdateView.as_view(), name="post_update"),
	path("delete/<str:pk>", PostDeleteView.as_view(), name="post_delete"),

]