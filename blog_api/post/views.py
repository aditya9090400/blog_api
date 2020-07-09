from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import (IsAuthenticated,
										AllowAny,
										IsAdminUser,
										IsAuthenticatedOrReadOnly
										)
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer
from post.models import Post
# print(dir(permissions))

class PostCreateView(generics.CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class PostListView(generics.ListAPIView):
	permission_classes = [IsAdminUser]
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title']
	pagination_class = PostPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		# query_list = super(PostListView, self).get_queryset(*args, **kwargs)
		query_list = Post.objects.all()
		query = self.request.GET.get("q", None)
		if query:
			query_list = query_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(slug__icontains=query)|
				Q(user__first_name__icontains=query)|
				Q(user__last_name__icontains=query)
				).distinct()
		return query_list

class PostUpdateView(generics.RetrieveUpdateAPIView):#:UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
	# lookup_field = 'slug'

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class PostDeleteView(generics.DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer


class PostDetailView(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug' 