from django.db import models

# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length = 50)
    create_at = models.DateTimeField()


class tag(models.Model):
    tag_name = models.CharField(max_length = 50)
    create_at = models.DateTimeField()

class articles(models.Model):
    key_word = models.CharField(max_length=255)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    cid = models.IntegerField()
    tags = models.CharField(max_length = 255)
    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class comments(models.Model):
    uid = models.IntegerField()
    title = models.CharField(max_length= 255)
    content = models.TextField()
    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class comment(models.Model):
    uid = models.IntegerField()
    title = models.CharField(max_length= 255)
    content = models.TextField()
    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()