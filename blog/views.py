# -*- coding: utf8 -*-
from django.shortcuts import render
from .models import Category, Post, Link, Image
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })
