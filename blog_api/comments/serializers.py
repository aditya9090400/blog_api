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

class CommentChildSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = [
			'id',
			'content',
			'timestamp',
		]

class CommentDetailSerializer(serializers.ModelSerializer):
	replies = serializers.SerializerMethodField()	
	class Meta:
		model = Comment
		fields = [
			'id',
			'user',
			'content_type',
			# 'object_id ',
			# 'content_object',
			'parent',
			'content',
			'timestamp',
			'replies'
		]
	def get_replies(self, obj):
		print(obj.parent)
		if obj.parent:
			return CommentChildSerializer(obj.children(),many=True).data
		return None