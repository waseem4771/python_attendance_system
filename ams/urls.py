"""
URL configuration for ams project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from main import views ,admin_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),

    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('edit_profile_picture/', views.edit_profile_picture, name='edit_profile_picture'),

    path('admin_dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('view_user_attendance/<int:user_id>', admin_views.view_user_attendance, name='view_user_attendance'),
    path('edit_attendance/<int:attendance_id>/', admin_views.edit_attendance, name='edit_attendance'),
    path('delete_attendance/<int:attendance_id>/', admin_views.delete_attendance, name='delete_attendance'),
    path('leave_approval/', admin_views.leave_approval, name='leave_approval'),
    path('system_report/', admin_views.system_report, name='system_report'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)