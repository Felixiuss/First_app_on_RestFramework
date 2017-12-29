# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
