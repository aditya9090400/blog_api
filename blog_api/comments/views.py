from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import (IsAuthenticated,
										AllowAny,
										IsAdminUser,
										IsAuthenticatedOrReadOnly
										)
from rest_framework.filters import SearchFilter,OrderingFilter
from blog_api.post.pagination import PostPageNumberPagination
from blog_api.post.permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer
from comments.models import Comment
# print(dir(permissions))

# class PostCreateView(generics.CreateAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateSerializer
# 	permission_classes = [IsAuthenticated]

# 	def perform_create(self, serializer):
# 		serializer.save(user=self.request.user)


class CommentListAPIView(generics.ListAPIView):
	permission_classes = [IsAdminUser]
	serializer_class = CommentSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	# search_fields = ['title']
	pagination_class = PostPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		# query_list = super(PostListView, self).get_queryset(*args, **kwargs)
		query_list = Comment.objects.all()
		query = self.request.GET.get("q", None)
		if query:
			query_list = query_list.filter(
				
				Q(content__icontains=query)|
				
				Q(user__first_name__icontains=query)|
				Q(user__last_name__icontains=query)
				).distinct()
		return query_list

# class PostUpdateView(generics.RetrieveUpdateAPIView):#:UpdateAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostCreateSerializer
# 	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
# 	# lookup_field = 'slug'

# 	def perform_update(self, serializer):
# 		serializer.save(user=self.request.user)

# class PostDeleteView(generics.DestroyAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostListSerializer


class CommentDetailAPIView(generics.RetrieveAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer