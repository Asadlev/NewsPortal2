from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import News
from .filters import NewsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin


class NewsListView(ListView):
    model = News
    ordering = 'author'
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 2

    # Переопределяем функцию получения списка новостей
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список Новостей
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context




class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'new'


class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # Модель новостей
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


class NewsUpdate(LoginRequiredMixin, UpdateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # Модель новостей
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_update.html'

    def get_success_url(self):
        return reverse_lazy('news_detail', kwargs={'pk': self.object.pk})





class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')




