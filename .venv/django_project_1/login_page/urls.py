from django.contrib import admin
from django.urls import path
from.import views as VS

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('loginform/', VS.registration ),
]