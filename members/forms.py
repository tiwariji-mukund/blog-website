from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from my_blogs.models import UserProfile

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)
	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['password1'].widget.attrs['class'] = 'form-control'
	    self.fields['password2'].widget.attrs['class'] = 'form-control'

class UpdateProfileForm(UserChangeForm):
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password', 'last_login', 'date_joined')

class ChangePasswordForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('bio', 'profile_pic', 'web_url', 'fb_url', 'instagram_url', 'linkedin_url', 'whatsapp_url')
		widgets = {
	        'bio': forms.Textarea(attrs={'class': 'form-control'}),
	        # 'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
	        'web_url': forms.TextInput(attrs={'class': 'form-control'}),
	        'fb_url': forms.TextInput(attrs={'class': 'form-control'}),
	        'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
	        'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
	        'whatsapp_url': forms.TextInput(attrs={'class': 'form-control'}),
	        }