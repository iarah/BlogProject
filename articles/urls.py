from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
]