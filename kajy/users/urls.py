from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView


app_name = 'users_app'
urlpatterns = [
	path('inscription/', views.inscription, name = 'inscription'),
	path('connexion/', LoginView.as_view(template_name = 'users/connexion.html'), name = 'connexion'),
	path('deconnexion/', LogoutView.as_view(template_name = 'users/deconnexion.html'), name = 'deconnexion'),
	path('profile/<int:pk>', views.SeeProfile.as_view(), name = "profile"),
	path('profile/<int:pk>/modifier/personal/', views.ChangeInfo.as_view(),name = "personal"),
	path('profile/<int:pk>/modifier/user/', views.ChangeUser.as_view(),name = "user"),
	path('profile/<int:pk>/modifier/avatar/', views.ChangeAvatar.as_view(),name = "avatar"),
]