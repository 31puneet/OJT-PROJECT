from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_page, name='create_page'),
    path('edit/<int:page_id>/', views.edit_page, name='edit_page'),
    path('delete/<int:page_id>/', views.delete_page, name='delete_page'),
    path('history/<int:page_id>/', views.history_list, name='history'),
    path('', lambda request: redirect('/dashboard/')),
    
    # === CORRECT URL PATTERN ===
    path('compare/', views.compare_view, name='compare'),
    
    path('restore/<int:version_id>/', views.restore_version, name='restore'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
