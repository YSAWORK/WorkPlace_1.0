from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from VBworkspace import settings

urlpatterns = [
    path('Employees/', include('Employees.urls')),
    path('Clients/', include('Clients.urls')),
    path('admin/', admin.site.urls),]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
