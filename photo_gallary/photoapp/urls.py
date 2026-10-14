from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('tag/<int:tag_id>/', views.filter_tag, name='filter_tag'),
    path('photo/<int:photo_id>/react/', views.photo_reaction_view, name='photo_reaction'),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )