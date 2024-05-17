from django.contrib import admin
from django.urls import path,include

urlspatterns = [
    path('admins/', admin.site.urls),
    path('', include('recipes.urls')),
    path('recipes/', include('recipes.urls'))
]







