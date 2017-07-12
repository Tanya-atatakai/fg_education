from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import BlogPost


paginate_by = 6


def education_blog_post_list(request):
    """
    отображает список постов с пагинацией. Количество постов на страницу
    в параметре paginate_by
    """
    post_list = BlogPost.objects.published()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, paginate_by)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blogpost_list.html', {'posts': posts})


class PostDetailView(DetailView):
    """
    рендерит детальное отображение поста
    """
    model = BlogPost
