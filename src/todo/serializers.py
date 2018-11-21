from rest_framework import serializers
from todo.model import TodoItem

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.ReadOnlyField()
	class Meta:
		model = TodoItem
		fields = ('url','title','completed','order')