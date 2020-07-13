from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Comment
		fields = [
			'id',
			
			'user',
			'content_type',
			# 'object_id ',
			'content_object',
			'parent',
			'content',
			'timestamp',
		]