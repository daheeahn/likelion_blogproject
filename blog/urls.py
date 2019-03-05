from django.contrib import admin
from django.urls import path
# import blog.views, portfolio.views # 아래와 같음
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
]