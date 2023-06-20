from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["id","name"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # status field is a mandatory field.
    status = serializers.ChoiceField(
        choices=Task.STATUS_CHOICES, required=True)

    # tags should be shown as tags name instead of urls.
    tags = serializers.SlugRelatedField(
        slug_field='name', queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Task
        fields = ["id", "status", "timestamp",
                  "title", "description", "due_date", "tags"]
        read_only_fields = ['id', 'timestamp']

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if tags_data is not None:
            instance.tags.set(tags_data)

        instance.save()

        return super().update(instance, validated_data)
