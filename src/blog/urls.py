from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('blog/', views.Blog, name='blog'),
    path('<slug:slug>', views.single_post, name='single_post'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)