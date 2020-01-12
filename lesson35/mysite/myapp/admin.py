from django.contrib import admin
from .models import Article,Comment,Profile,Like


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Like)