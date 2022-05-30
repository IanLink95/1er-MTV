from django.contrib import admin
from django.urls import path
from registrodefamiliares.views import familiar1,familiar2,familiar3,familiar4,nacionalidad1,nacionalidad2,nacionalidad3,familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiar1/',familiar1),
    path('familiar2/',familiar2),
    path('familiar3/',familiar3),
    path('familiar4/',familiar4),
    path('nacionalidad1/',nacionalidad1),
    path('nacionalidad2/',nacionalidad2),
    path('nacionalidad3/',nacionalidad3),
    path('home/',familiares),
]
