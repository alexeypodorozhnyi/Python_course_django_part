from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='', null=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username


class Article(models.Model):
    name = models.CharField(max_length=100, default='My article')
    text = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default='')
    parent_comment = models.ForeignKey("self",null=True, blank=True, on_delete=models.DO_NOTHING)

    def children(self):
        return Comment.objects.filtered(parent_comment=self)

    @property
    def is_parent(self):
        if self.parent_comment is not None:
            return False
        return True


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default='')
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, default='')
