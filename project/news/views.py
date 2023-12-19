from django.shortcuts import render, get_object_or_404
from django.template import Library
from .models import News


register = Library()


@register.filter(name='censor')
def censor(value):
    unwanted_words = ["нежелательное", "еще одно"]  # Замените это на список нежелательных слов
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))
    return value

def news_list(request):
    news_list = News.objects.order_by('-pub_date')
    return render(request, 'news_list.html', {'news_list': news_list, 'censor': censor})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    news_item.text = censor(news_item.text)
    return render(request, 'news_detail.html', {'news_item': news_item, 'censor': censor})
