from rest_framework import serializers
from post.models import Post

post_detail_url = serializers.HyperlinkedIdentityField(view_name='post_detail', lookup_field="slug")
post_delete_url = serializers.HyperlinkedIdentityField(view_name='post_delete', lookup_field="pk")	

class PostListSerializer(serializers.ModelSerializer):
	url = post_detail_url
	class Meta:
		model = Post
		fields = [
			'id',
			'url',
			'user',
			'title',
			'content',
			'publish',
		]

class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			# 'user',
			'title',
			'content',
			'publish',
			'slug'
		]

class PostDetailSerializer(serializers.ModelSerializer):
	delete_url = post_delete_url
	image_url = serializers.SerializerMethodField()
	user_name = serializers.SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'id',
			'user_name',
			'delete_url',
			'image_url',
			'title',
			'content',
			'publish',
			'slug'
		]

	def get_user_name(self, obj):
		return obj.user.username
	def get_image_url(self, obj):
		try:
			image_url = obj.image.url
		except:
			image_url = None 
		return image_url

