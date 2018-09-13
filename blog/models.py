from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import ImageField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    category = models.ForeignKey(Category, default='0', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.TextField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, default='0')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    imgUrl = ImageField(upload_to='PostImg', default='0')

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title


class TopPost(models.Model):
    title = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    imgUrl = ImageField(upload_to='TopPostImg')

    def __str__(self):
        return self.title
