from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('work_detail/<int:id>', views.work_detail, name='work_detail'),
	path('register', views.register, name='register'),
]