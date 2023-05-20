from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:user_id>/', views.userContent, name='userContent'),
    path('<username>/profile/', views.profile, name="profile"),
    path('<username>/profile/follow/', views.follow, name="follow"),
    # path('uniquecheck/username', views.UsernameUniqueCheck.as_view(), name='uniquecheck_username'),
]
