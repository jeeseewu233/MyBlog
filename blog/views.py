from django.shortcuts import render, get_object_or_404
from . import models
import markdown
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    page_num = 10
    all_post_list = models.Post.objects.all().order_by('-created_time')
    sum_num = all_post_list.count()
    top_post_list = models.TopPost.objects.all()[:3]
    most_view_list = all_post_list.order_by("-views")[:5]

    paginator = Paginator(all_post_list, page_num)
    current_page = 1
    previous_page = current_page - 1
    next_page = current_page + 1
    post_list = paginator.page(current_page)
    context = {
        "post_list": post_list,
        "top_post_list": top_post_list,
        "most_view_list": most_view_list,
        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.fenced_code',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    all_post_list = models.Post.objects.all().order_by('-created_time')
    most_view_list = all_post_list.order_by("-views")[:5]

    # comment_list = post.comments_set.filter(post=post).order_by("-created_time")
    context = {
        "post": post,
        "most_view_list": most_view_list
        # "comment_list": comment_list
    }
    return render(request, "blog/detail.html", context)


def category(request, category_id):
    page_num = 10
    category_name = models.Category.objects.get(pk=category_id)
    all_post_list = models.Post.objects.filter(category__name=category_name).order_by("-created_time")
    sum_num = all_post_list.count()
    most_view_list = all_post_list.order_by("-views")[:5]
    tag_list = models.Tag.objects.all().filter(category__name=category_name)[:3]
    bigTitle = category_name

    paginator = Paginator(all_post_list, page_num)
    current_page = 1
    previous_page = current_page - 1
    next_page = current_page + 1
    post_list = paginator.page(current_page)
    context = {
        "post_list": post_list,
        "bigTitle": bigTitle,
        "tag_list": tag_list,
        "most_view_list": most_view_list,
        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num,
        "category_id": category_id
    }
    return render(request, 'blog/list.html', context)


def tag(request, tag_id):
    page_num = 10
    tag_name = models.Tag.objects.get(pk=tag_id)
    all_post_list = models.Post.objects.filter(tags__name=tag_name).order_by("-created_time")
    sum_num = all_post_list.count()
    most_view_list = all_post_list.order_by("-views")[:5]
    bigTitle = tag_name

    paginator = Paginator(all_post_list, page_num)
    current_page = 1
    previous_page = current_page - 1
    next_page = current_page + 1
    post_list = paginator.page(current_page)
    context = {
        "post_list": post_list,
        "bigTitle": bigTitle,
        "most_view_list": most_view_list,

        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num,
        "tag_id": tag_id
    }
    return render(request, 'blog/tag.html', context)


def top(request):
    page_num = 10
    all_post_list = models.Post.objects.all().order_by("-views")
    sum_num = all_post_list.count()

    paginator = Paginator(all_post_list, page_num)
    current_page = 1
    previous_page = current_page - 1
    next_page = current_page + 1
    post_list = paginator.page(current_page)
    context = {
        "post_list": post_list,
        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num
    }
    return render(request, 'blog/top.html', context)


def page(request, current_page):
    page_num = 10
    all_post_list = models.Post.objects.all().order_by('-created_time')
    sum_num = all_post_list.count()
    top_post_list = models.TopPost.objects.all()[:3]
    most_view_list = all_post_list.order_by("-views")[:5]

    paginator = Paginator(all_post_list, page_num)
    # current_page = request.GET.get('page')
    previous_page = current_page - 1
    next_page = current_page + 1
    try:
        post_list = paginator.page(current_page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
        "top_post_list": top_post_list,
        "most_view_list": most_view_list,
        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num
    }
    return render(request, "blog/index.html", context)


def category_page(request, category_id, current_page):
    page_num = 10
    category_name = models.Category.objects.get(pk=category_id)
    all_post_list = models.Post.objects.filter(category__name=category_name).order_by("-created_time")
    sum_num = all_post_list.count()
    most_view_list = all_post_list.order_by("-views")[:5]
    tag_list = models.Tag.objects.all().filter(category__name=category_name)[:3]
    bigTitle = category_name

    paginator = Paginator(all_post_list, page_num)
    # current_page = request.GET.get('page')
    previous_page = current_page - 1
    next_page = current_page + 1
    try:
        post_list = paginator.page(current_page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
        "bigTitle": bigTitle,
        "tag_list": tag_list,
        "most_view_list": most_view_list,
        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num,
        "category_id": category_id
    }
    return render(request, "blog/list.html", context)


def tag_page(request, tag_id, current_page):
    page_num = 10
    tag_name = models.Tag.objects.get(pk=tag_id)
    all_post_list = models.Post.objects.filter(tags__name=tag_name).order_by("-created_time")
    sum_num = all_post_list.count()
    most_view_list = all_post_list.order_by("-views")[:5]
    bigTitle = tag_name

    paginator = Paginator(all_post_list, page_num)
    # current_page = request.GET.get('page')
    previous_page = current_page - 1
    next_page = current_page + 1
    try:
        post_list = paginator.page(current_page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
        "bigTitle": bigTitle,
        "most_view_list": most_view_list,
        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num,
        "tag_id": tag_id
    }
    return render(request, "blog/tag.html", context)


def top_page(request, current_page):
    page_num = 10
    all_post_list = models.Post.objects.all().order_by("-views")
    sum_num = all_post_list.count()

    paginator = Paginator(all_post_list, page_num)
    # current_page = request.GET.get('page')
    previous_page = current_page - 1
    next_page = current_page + 1
    try:
        post_list = paginator.page(current_page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        "post_list": post_list,
        "paginator": paginator,
        "current_page": current_page,
        "previous_page": previous_page,
        "next_page": next_page,
        "sum_num": sum_num
    }
    return render(request, "blog/top.html", context)
