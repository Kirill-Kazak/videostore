from django.test import TestCase, Client
from .models import Video, Comment
from django.contrib.auth.models import User



class TestVideo(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="username",
            email="email",
            password="password")
        User.objects.create_superuser(
            username="superuser",
            email="superemail",
            password="superpassword"
        )
        self.client=Client()
        v = Video.objects.create(
            slug='test slug',
            urls='test url',
            title='test title',
            description='test description')
        Comment.objects.create(
            text='test text',
            comment_video_id=v.id)

    def test_first(self):
        v = Video.objects.all()[0]
        c = v.comment.all()[0]
        self.assertEqual(c.text, "test text")
    
    
    def test_page_enabled(self):
        response = self.client.get("/hello/456/")
        self.assertEqual(response.status_code, 200)
        
    def test_admin_login(self):
        res = self.client.login(
            username="username",
            # email="email",
            password="password"
        )
        self.assertEqual(res, True)
        
    def test_login_admin(self):
        self.client.login(
            username="superuser",
            # email="superemail",
            password="superpassword")
        res = self.client.get("/admin/showvideo/video/")
        self.assertEqual(res.status_code, 200)
        
    def test_property(self):
        v = Video.objects.get(id=1)
        self.assertEqual(v.test, "hello test title0")


