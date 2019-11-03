from django.shortcuts import render, get_object_or_404
from .models import post
from django.utils import timezone


# Create your views here.

def post_list(request):
    posts = post.objects.filter(title__contains="blog").order_by("published_date")
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    pos = get_object_or_404(post, pk=pk)
    return render(request, 'blog/post_detail.html', {'pos': pos})
