from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    # path('article/', views.AllArticleAPIView.as_view(), name='all_articles'),
    # path('article/', views.SingleArticleAPIView.as_view(), name='single_article'),
    path('article/', views.AllArticleView.as_view(), name='all_article'),
    path('article/<int:pk>', views.DetailArticleView.as_view(), name='detail_article'),
]
