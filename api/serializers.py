from rest_framework import serializers
from .models import Task, Tag
from django.urls import reverse

from rest_framework.response import Response
# class TaskSerializer(serializers.ModelSerializer):


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # tags = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all(),
    #     view_name='tag-detail',
    #     required=False,
    # )
    # tags = serializers.ListField(child=serializers.CharField(), required=False)

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

    # def create(self, instance, validated_data):

    #     return super().update(instance, validated_data)

    # def get_tag_id_from_url(self, tag_url):
    #     try:
    #         tag_id = int(tag_url.split('/')[-2])
    #         return tag_id
    #     except (ValueError, IndexError):
    #         return None
    # def update(self, instance, validated_data):
    #     for field, value in validated_data.items():
    #         if value is not None:
    #             setattr(instance, field, value)
    #     instance.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     # Exclude 'description' from validated_data if not provided during update
    #     if 'description' not in validated_data:
    #         validated_data.pop('description', None)
    #     return super().update(instance, validated_data)

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'timestamp', 'title', 'description', 'due_date', 'tag', 'status']
#         read_only_fields = ['id', 'timestamp']
