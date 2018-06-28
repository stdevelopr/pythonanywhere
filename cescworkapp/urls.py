from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('work_detail/<int:id>', views.work_detail, name='work_detail'),
	path('register', views.register, name='register'),
	path('my_works', views.my_works, name='my_works'),
	path('create_work', views.create_work, name='create_work'),
	path('edit_work/<int:id>', views.edit_work, name='edit_work'),

]