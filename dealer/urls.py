from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# from  import project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
]
