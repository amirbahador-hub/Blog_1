from django.shortcuts import render
from .models import Post


def index(request):
    queryset = Post.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})


def new_post(request):
    return render(request, 'new_post.html', {})


def single(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'single.html', context)

#     latest_post = Post.objects.order_by('-published')[:1]
#
#     context = {
#         'latest_post': latest_post
#     }
    # return render(request, 'index.html', context)