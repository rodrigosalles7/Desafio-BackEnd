from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/proj/', include("proj.urls")),
    path('docs/', include_docs_urls(title='Proj Api')),
]
