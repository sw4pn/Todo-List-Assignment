from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status


from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from .serializers import TaskSerializer, TagSerializer
from .models import Task, Tag

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAuthenticated]

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

    #     # Extract the tags arr from the request data
    #     tags_arr = request.data.get('tags', [])

    #     request.data['tags'] = []

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # Save the task
    #     self.perform_create(serializer)
    # Check if each tag exists in Tag model, create if not
    # tags = []

    # for tag_name in tags_arr:
    #     tag_name = tag_name.lower()
    #     tag, created = Tag.objects.get_or_create(name=tag_name)
    #     if created:
    #         tags.append({"name": tag.name})
    #     else:
    #         tags.append({"name": tag_name})

    # # Add the tags to the request data
    # request.data["tags"] = tags

    # def update(self, instance, validated_data):
    #     #     print("updating code...")
    #     tags_data = validated_data.pop('tags', None)

    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)

    #     if tags_data is not None:
    #         tags = []

    #         for tag_name in tags_data:
    #             tag_name = tag_name.lower()
    #             tag, created = Tag.objects.get_or_create(name=tag_name)
    #             url_path = reverse('tag-detail', kwargs={'pk': tag.pk})
    #             # Get the request object from the context
    #             request = self.context.get('request')
    #             tags.append(request.build_absolute_uri(url_path))
    #             # print(tag.pk)
    #             # tags.append(tag.pk)
    #             # tag_url = request.build_absolute_uri(reverse('tag-detail', kwargs={'pk': tag.pk}))
    #             # tags.append(tag_url)

    #         print("tags", tags)
    #         instance.tags.set(tags)
    #     instance.save()

    #     return super().update(instance, validated_data)


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     ser = self.serializer_class(data=request.data)
    #     ser.is_valid()
    #     print(ser.errors)  # force to show errors
    #     return super().create(request, *args, **kwargs)

# @api_view(["GET"])
# def apiOverview(request):
#     api_urls = {
#         'List': '/todo-list/',
#         'Detail View': '/todo-detail/<str:pk>/',
#         'Create': '/todo-create/',
#         'Update': '/todo-update/<str:pk>/',
#         'Delete': '/todo-delete/<str:pk>/',
#     }
#     return Response(api_urls)


# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         task = serializer.save()
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# # class TaskList(generics.ListCreateAPIView):
# #     queryset = Task.objects.all()


# @api_view(["GET"])
# def todoList(request):
#     todo_list = Task.objects.all()
#     serializer = TaskSerializer(todo_list, many=True)
#     return Response(serializer.data)


# @api_view(["GET"])
# def todoDetail(request, id):
#     todo = Task.objects.get(id=id)
#     serializer = TaskSerializer(todo, many=True)
#     return Response(serializer.data)


# @api_view(["POST"])
# def todoCreate(request):
#     if (request.method == "GET"):
#         todo = Task.objects.all()
#         serializer = TaskSerializer(todo, many=True)
#         return Response(serializer.data)
#     if (request.method == "POST"):
#         data = {
#             "title": request.data.get("title"),
#             "content": request.data.get("content"),
#             "completed": request.data.get("completed")
#         }
#         serializer = TaskSerializer(data=data)
#         # return Response(serializer)
