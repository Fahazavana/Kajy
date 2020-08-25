from django.urls import path
from . import views
app_name = 'forum_app'
urlpatterns = [
	path('', views.HomeView.as_view(), name = "home"),
	path('apropos/', views.AboutView.as_view(), name = 'about'),
	path('create/', views.CreatePost.as_view(), name='create_post' ), #C
	path('detail/<int:pk>/', views.ReadPost.as_view(), name = 'read_post'), #R
	path('detail/<int:pk>/maj', views.UpdatePost.as_view(), name='update_post' ), #U
	path('detail/<int:pk>/suprimer', views.SuprQuestion.as_view(), name='delete_post' ), #D
	path('detail/<int:pk>/comment', views.commenter, name = 'add_comment_post'),
	path('detail/<int:pk>/voter', views.voter, name = 'voter'),
]
