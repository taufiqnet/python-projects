
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


#to go views.py
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #custom paths > views.py > function - homepage
    path('', views.homepage, name='home'),
    path('word/', views.wordcount, name='word'),
    path('contact/', views.contact),
    path('about/', views.about, name='about'),
    path('count/', views.count, name='count'),
    
    #Function Based Application
    path('tasks/', include('tasks.urls'), name='tasks'),
    
    #Class Based Applicaiton
    path('taskList', include('base.urls')),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
