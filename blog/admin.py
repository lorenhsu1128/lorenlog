# -*- coding: utf8 -*-
"""

"""
from django.contrib import admin
from .models import Category, Post, Link, Image
from django import forms
from ckeditor.widgets import CKEditorWidget


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'seq', 'update_time']


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        exclude = []

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'slug', 'body', 'update_time']
    form = PostAdminForm
    save_as = True

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'title', 'type', 'body', 'update_time']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'title','thumbnail', 'size', 'dimensions', 'update_time']
    # exclude = ('image_tag',)
    readonly_fields = ('thumbnail', 'size', 'dimensions', )


