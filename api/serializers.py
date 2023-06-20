from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['id', 'timestamp']

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if tags_data is not None:
            instance.tags.set(tags_data)

        instance.save()

        return super().update(instance, validated_data)
