from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    queryset = Post.objects.filter(featured=True)
    most_recent = queryset.order_by('-created')
    paginator = Paginator(most_recent, 1)
    page_req = 'page'
    page = request.GET.get(page_req)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        return render(request, 'page_404.html', {})
        # paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'most_recent': most_recent,
        'queryset': paginated_queryset,
        'page_req': page_req,
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

#
# def error_404(request , exception):
#     data = {}
#     return render(request, 'page_404.html', data)
#
#
# def error_500(request, exception):
#     data = {}
#     return render(request, 'page_500.html', data)
#     latest_post = Post.objects.order_by('-published')[:1]
#
#     context = {
#         'latest_post': latest_post
#     }
    # return render(request, 'index.html', context)