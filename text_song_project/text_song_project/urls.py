"""
URL configuration for text_song_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from song.views import home, generate_audio  # Apni app ka naam sahi likhein
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),  # Ye aapka main page hai
#     path('generate-audio/', generate_audio, name='generate_audio'),
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ]

# # Media files ke liye rasta - Ye urlpatterns ke BAAD hona chahiye
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# second code of mmy project ========
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# from text_song_project.song import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('song.urls')),  # agar aapke song app ke alag urls hain
#     path('', views.home, name='home'),

# ]

# # Development mein media files serve karne ke liye
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









# =========seond code with seo =========



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('song.urls')),  # Song app ke URLs include karein
]

# Development mein media files serve karne ke liye
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)