# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route


class SnippetViewSet(viewsets.ModelViewSet):
    """
    Этот viewset автоматически предоставляет действия `list`,` create`, `retrieve`,` update` и `destroy`.
    Кроме того, мы также предоставляем дополнительное действие `highlight`.
    Эта конечная точка содержит фрагменты кода.
    Поле `highlight` представляет собой гиперссылку на выделенный HTML-код представление фрагмента кода.
    владелец фрагмента кода может обновлять или удалять экземпляры фрагмента кода
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Эта конечная точка представляет пользователей в системе.
    Этот набор представлений автоматически создает действия `list` и `detail`.
    Как вы можете видеть, коллекция экземпляров фрагмента, принадлежащих пользователю,
    сериализован с использованием гиперссылки.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
