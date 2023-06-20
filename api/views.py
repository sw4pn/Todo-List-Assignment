from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated

from .serializers import TaskSerializer, TagSerializer
from .models import Task, Tag


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    #   Convert the tags from string to hyperlinks
    @staticmethod
    def updateTags(tags_array, request):
        tags = []
        for tag_name in tags_array:
            tag_name = tag_name.lower()
            tag, created = Tag.objects.get_or_create(name=tag_name)
            url_path = reverse('tag-detail', kwargs={'pk': tag.pk})
            tags.append(request.build_absolute_uri(url_path))
        return tags

    # update tags and pass data for update
    def update(self, request, *args, **kwargs):
        tags_arr = request.data.get('tags', None)

        if tags_arr is not None:
            request.data['tags'] = self.updateTags(tags_arr, request)

        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        tags_arr = request.data.get('tags', None)

        if tags_arr is not None:
            request.data['tags'] = self.updateTags(tags_arr, request)

        return super().create(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
