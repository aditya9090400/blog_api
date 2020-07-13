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

'''
blog-api
https://www.youtube.com/watch?v=58p_mNuntd8&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=20&t=0s
https://www.youtube.com/watch?v=CU4qv7cSnmA&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=20
https://www.youtube.com/watch?v=vn0XVNzkJvc&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=21
https://www.youtube.com/watch?v=DX3ekF1Xx8U&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=22
https://www.youtube.com/watch?v=TRcVXGL1MjI&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=23
https://www.youtube.com/watch?v=mhWvk7vyru0&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=24
https://www.youtube.com/watch?v=B7bdoLMQrJY&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=25
https://www.youtube.com/watch?v=fvMLvFnEBBM&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=26
https://www.youtube.com/watch?v=5dtbbImcUCI&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=27
https://www.youtube.com/watch?v=gNXnDlfYOqA&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=28
https://www.youtube.com/watch?v=0jSzFUZ__k8&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=29
https://www.youtube.com/watch?v=bDwDOatEihw&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=30
https://www.youtube.com/watch?v=e5aL6jy4NwA&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=31
https://www.youtube.com/watch?v=jEXQqNtjNJc&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=32
https://www.youtube.com/watch?v=mi-AcUdGxxs&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS&index=33
'''