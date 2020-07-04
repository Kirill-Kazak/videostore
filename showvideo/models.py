from django.db import models
from django.utils.safestring import mark_safe


class Video(models.Model):       # A 1      B   2     C  3
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "много видео"

    slug = models.SlugField(
        unique=False,
        verbose_name="Слаг",
        help_text="слаг должен быть уникальным"
    )
    urls = models.URLField(verbose_name="Урл, понял?")
    title = models.CharField(max_length=150, verbose_name="название")
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата")
    description = models.TextField(
        verbose_name="описание",
        null=True,
        blank=True)
    likes = models.PositiveIntegerField(default=0, verbose_name="нравится)")

    def __str__(self):
        return self.title

    @property
    def test(self):
        return f"hello {self.title}{self.likes ** 2}"

    @property
    def tv(self):
        return mark_safe(f"<iframe width='100' height='50' src='{self.urls}'></iframe>")
# url_a, ..... 1
# url_b, ..... 2
# url_c, ..... 3


class Comment(models.Model):   # 1 - 5шт    2 - 3 шт
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comment")

# text_a,..,id, comment_video_id = 1
# text_b,..,id, comment_video_id = 1
# text_c,..,id, comment_video_id = 1
# text_a,..,id, comment_video_id = 2
# text_b,..,id, comment_video_id = 2
# text_c,..,id, comment_video_id = 3

