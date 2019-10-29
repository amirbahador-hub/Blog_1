from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Post
from django.http import HttpResponse

#
def index(request):
    return HttpResponse("Hello World!")
#
# def single(request):
#     return render(request, 'single.html', {})

#     latest_post = Post.objects.order_by('-published')[:1]
#
#     context = {
#         'latest_post': latest_post
#     }
    # return render(request, 'index.html', context)