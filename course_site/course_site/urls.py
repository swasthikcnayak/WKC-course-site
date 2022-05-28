from django.contrib import admin
from course_site.course_site import settings
from django.conf.urls.static import static
from .views import index
from django.urls import path, include
import course_site.users.urls as users_url
import course_site.courses.urls as course_url

handler404 = 'course_site.course_site.views.handler404'
handler500 = 'course_site.course_site.views.handler500'
handler400 = 'course_site.course_site.views.handler400'
handler403 = 'course_site.course_site.views.handler403'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/', include(users_url)),
    path('courses/',include(course_url))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

