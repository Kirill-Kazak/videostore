from django.contrib import admin
from .models import Video, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment


class VideoAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]
    readonly_fields = ["likes"]
    list_display = ["title", "likes", "test", "tv"]
    list_filter = ["likes", "date"]
    prepopulated_fields = {"slug":["title"]}
    search_fields = ["date"]


admin.site.register(Video, VideoAdmin)
# admin.site.register(Comment)
# Register your models here.
