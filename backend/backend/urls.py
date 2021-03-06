from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('article.api.urls'))
]
