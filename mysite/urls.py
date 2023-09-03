# urlpatterns 미디어 경로 설정. img link
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    #kkk
    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
