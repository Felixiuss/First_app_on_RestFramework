# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Создание маршрутизатора и регистрация наших представлений с ним.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# Теперь URL-адреса API автоматически определяются маршрутизатором.
urlpatterns = [
    url(r'^', include(router.urls))
]
