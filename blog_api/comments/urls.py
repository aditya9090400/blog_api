from django.urls import path


from .views import (
    CommentListAPIView,
    CommentDetailAPIView

    )



urlpatterns = [
	path("", CommentListAPIView.as_view(), name="list"),
	path("<int:pk>/", CommentDetailAPIView.as_view(), name="thread"),

	# path("create", PostCreateView.as_view(), name="post_create"),
	# path("<str:slug>", PostDetailView.as_view(), name="post_detail"),
	# path("update/<str:pk>", PostUpdateView.as_view(), name="post_update"),
	# path("delete/<str:pk>", PostDeleteView.as_view(), name="post_delete"),

]
# urlpatterns = [
#     path(, CommentListAPIView.as_view(), name='list'),
#     url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
#     #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
# ]