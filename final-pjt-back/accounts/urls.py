from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup),
    # path('uniquecheck/username', views.UsernameUniqueCheck.as_view(), name='uniquecheck_username'),
]
