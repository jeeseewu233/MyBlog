from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_time", "category", "author")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.User)
admin.site.register(models.TopPost)
