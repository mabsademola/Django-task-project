
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users.router import router
from house import router as house_api_urls
from taskapp import router as taskapp_api_urls



auth_api_urls = [
    path(r'',include('drf_social_oauth2.urls')),
  
]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))


api_urls_patterns = [
path(r'accounts/', include(router.urls)),
path(r'auth/', include(auth_api_urls)),
path(r'house/', include(house_api_urls.router.urls)),
path(r'tasks/', include(taskapp_api_urls.router.urls)),
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls_patterns))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)