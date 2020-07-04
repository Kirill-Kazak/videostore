from rest_framework.serializers import ModelSerializer
from showvideo.models import Video, Comment


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class VideoSerializerB(ModelSerializer):
    class Meta:
        model = Video
        fields = ("urls", "title")# "__all__"


class CommentSerializer(ModelSerializer):
    comment_video = VideoSerializerB()
    class Meta:
        model = Comment
        fields = ("text", "date", "comment_video")#"__all__"

