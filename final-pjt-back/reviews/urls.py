from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.review_create),
    path('<int:review_pk>/', views.review_update_delete),
]