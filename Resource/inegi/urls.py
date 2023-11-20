from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #==================================#
    #           Applications           #
    #==================================#
    path('', include('wApp.urls')),
    path('', include('wINEGI.urls')),
]

# Rute images
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
