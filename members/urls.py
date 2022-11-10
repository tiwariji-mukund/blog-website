from django.urls import path
from .views import UserRegister, UserEdit, ChangePassword, MyProfilePage, ShowProfilePage, EditProfilePage, CreateProfilePage
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('register/', UserRegister.as_view(), name='register'),
	path('edit_settings/', UserEdit.as_view(), name='edit_settings'),
	# path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_pass.html')),
	path('password/', ChangePassword.as_view(template_name='registration/change_pass.html'), name='chage_pass'),
	path('password_success/', views.password_success, name='password_success'),
	path('<int:pk>/profile/', MyProfilePage.as_view(), name="profile"),
	path('<int:pk>/author/', ShowProfilePage.as_view(), name="profile_page"),
	path('<int:pk>/edit_profile/', EditProfilePage.as_view(), name="edit_profile"),
	path('create_profile/', CreateProfilePage.as_view(), name="create_profile"),


]
