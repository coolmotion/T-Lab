from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="shop"),
    path('audio/', views.home_audio, name="audio"),
    path('video/', views.home_video, name="video"),
    path('merchandising/', views.home_merchandising, name="merchandising"),
    path('used/', views.home_used, name="used"),
    path('product/<int:pk>', views.product, name="product"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register_user, name="register"),
    path('update_user', views.update_user, name="update_user"),
]
