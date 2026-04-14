from django.contrib import admin
from django.urls import path, include
from users.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timetable/', include('timetable.urls')),
    path('assignments/', include('assignments.urls')),
    path('tasks/', include('tasks.urls')),
    path('attendance/', include('attendance.urls')),
    path('exams/', include('exams.urls')),
    path('notes/', include('notes.urls')),
    path('files/', include('files.urls')),
    path('', include('dashboard.urls')),
    path('ai/', include('ai_assistant.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)