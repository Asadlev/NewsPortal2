from django.urls import path
from .views import NewsListView, NewsDetail, NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/news_detail/', NewsDetail.as_view(), name='news_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]









