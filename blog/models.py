# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import permalink
import os

class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='編號')
    title = models.CharField(max_length=255, db_index=True, verbose_name='標題')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='縮寫')
    seq = models.IntegerField(max_length=2, default=0, verbose_name='排序')
    update_time = models.DateField(db_index=True, auto_now_add=True, verbose_name='更新時間')

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

        class Meta:
            verbose_name = '分類'
            verbose_name_plural = '一堆分類'
            ordering = ['seq', '-update_time']


class Post(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='編號')
    title = models.CharField(max_length=255, unique=True, verbose_name='標題')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='縮寫')
    body = models.TextField(verbose_name='內容')
    update_time = models.DateField(db_index=True, auto_now_add=True, editable=False, verbose_name='更新時間')
    category = models.ForeignKey(Category, blank=True, null=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

        class Meta:
            verbose_name = '文章'
            verbose_name_plural = '一堆文章'
            ordering = ['-update_time']

class Link(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='編號')
    title = models.CharField(max_length=255, unique=True, verbose_name='標題')
    TYPE_CHOICES = (
        ('normal', '一般'),
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo'),
    )
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='normal', verbose_name='類型')
    body = models.CharField(max_length=255, verbose_name='連結')
    update_time = models.DateField(db_index=True, auto_now_add=True, editable=False, verbose_name='更新時間')
    post = models.ForeignKey(Post, blank=True, null=True)

    def __unicode__(self):
        return self.title

        class Meta:
            verbose_name = '連結'
            verbose_name_plural = '一堆連結'
            ordering = ['-update_time']

class Image(models.Model):
    """圖片"""

    id = models.AutoField(primary_key=True, verbose_name='編號')
    title = models.CharField(max_length=255, verbose_name='標題')

    full_path = os.path.realpath(__file__)
    img_dir = os.path.join((os.path.dirname(full_path)),'static/img')
    from django.core.files.storage import FileSystemStorage
    img_dir_fs = FileSystemStorage(location=img_dir)
    img_file = models.ImageField(storage=img_dir_fs, verbose_name='圖檔')

    update_time = models.DateTimeField(db_index=True, auto_now=True, editable=False, verbose_name='更新時間')
    post = models.ForeignKey(Post, blank=True, null=True)

    def thumbnail(self):
        """顯示縮圖的屬性
        admin一定要exclude = ('thumbnail',)
        readonly_fields = ('thumbnail',)
        """
        thumbnail = '<img src="%s" style="width:200px" />' % os.path.join('/static/img/',self.img_file.name.replace('./',''))
        return thumbnail
    thumbnail.short_description = '縮圖'
    thumbnail.allow_tags = True

    def size(self):
        size = '%sKB' % str(self.img_file.size/1024)
        return size
    size.short_description = '大小'
    size.allow_tags = True

    def dimensions(self):
        dimensions = '寬:%spx 高:%spx' % (self.img_file.width, self.img_file.height)
        return dimensions
    dimensions.short_description = '尺寸'
    dimensions.allow_tags = True

    def __unicode__(self):
        return self.title

        class Meta:
            verbose_name = '圖片'
            verbose_name_plural = '一堆圖片'
            ordering = ['-update_time']
