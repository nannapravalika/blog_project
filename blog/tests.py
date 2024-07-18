from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Post.objects.create(title='Test Post', content='Test Content', author=user)

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Post')

class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        Comment.objects.create(post=post, author='Test Author', text='Test Comment')

    def test_comment_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.text}'
        self.assertEqual(expected_object_name, 'Test Comment')
