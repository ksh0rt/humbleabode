from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from adobes import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('myabodes/', views.MyAbodes, name='my_abodes'),

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('addabode', views.AddAbode, name='add_abode'),
    path('abode/<int:pk>', views.DetailAbode, name='detail_abode'),
    path('abode/<int:pk>/update', views.UpdateAbode, name='update_abode'),
    path('abode/<int:pk>/delete', views.DeleteAbode.as_view(), name='delete_abode'),
    path('abode/<int:pk>/interested', views.Interested, name='interested'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
