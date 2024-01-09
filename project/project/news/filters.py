import datetime

# # filters.py
# from django import template
#
# register = template.Library()
#
# @register.filter(name='censor')
# def censor_filter(value):
#     # Заменяет буквы нежелательных слов на '*'
#     # Реализуйте свою логику для фильтрации
#     unwanted_words = ['нежелательное_слово1', 'нежелательное_слово2']
#     for word in unwanted_words:
#         value = value.replace(word, '*' * len(word))
#     return value

from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import News


class NewsFilter(FilterSet):
    # material = ModelMultipleChoiceFilter(
    #     field_name='name',
    #     queryset=Material.objects.all(),
    #     label='Material',
    #     conjoined=True,
    # )
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = News
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'author': ['icontains'],
            'title': ['gt'],
        }

    def get_date(self):
        context = super().get_date()
        date_ = datetime.datetime.utcnow()
        context['filterset'] = NewsFilter(self.request.GET)

        return context










