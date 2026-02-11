from django.contrib import admin
from django.urls import path, include
from api.views import api_root
from api.views.reviews import mongo_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', api_root),
    path('mongo-test/', mongo_test),
]
