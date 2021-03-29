from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
from django.core.paginator import Paginator


def news_home(request):
    news = Articles.objects.order_by('-date')
    paginator = Paginator(news, 3)
    page = request.GET.get('page')
    # ?page=2
    news = paginator.get_page(page)
    return render(request, 'news/news.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'
