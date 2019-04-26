from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('',views.home,name = 'welcome'),
    url(r'subscribe/', views.subscribe, name='subscribe'),

    
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)