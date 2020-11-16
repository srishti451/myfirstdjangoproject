
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('addpost',views.add_post,name='addpost'),
    path('update-post/<int:id>/',views.update_post,name='update'),
    path('delete-post/<int:id>/', views.delete_post,name='delete'),

    path('profile-settings',views.profile_settings,name='profile-settings')
    
]
if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
