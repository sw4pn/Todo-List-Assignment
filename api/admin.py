from django.contrib import admin
from .models import Task, Tag


@admin.action(description="Mark as OPEN")
def change_status_to_open(modeladmin, request, queryset):
    queryset.update(status="OPEN")


@admin.action(description="Mark as WORKING")
def change_status_to_working(modeladmin, request, queryset):
    queryset.update(status="WORKING")


@admin.action(description="Mark as DONE")
def change_status_to_done(modeladmin, request, queryset):
    queryset.update(status="DONE")


@admin.action(description="Mark as OVERDUE")
def change_status_to_overdue(modeladmin, request, queryset):
    queryset.update(status="OVERDUE")


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "status",
                    "due_date", "display_tags",  "description", "timestamp", ]
    list_filter = ["status", "tags"]
    # Task should be searched by tag.name field, title, description
    search_fields = ["title", "description", "tags__name"]

    actions = [change_status_to_open,
               change_status_to_done, change_status_to_working, change_status_to_overdue]

    fieldsets = [("Task Details*", {"fields": ["title", "description"]}),
                 ("Others", {"fields": ["due_date", "tags", "status"]})]

    # Extract tags and join tag.name by comma

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    display_tags.short_description = "Tags"


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]

    fieldsets = [("Enter Tag : ", {"fields": ["name"]})]


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
