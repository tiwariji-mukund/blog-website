from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateProfileForm, ChangePasswordForm, UserProfileForm
from django.contrib.auth.views import PasswordChangeView
from my_blogs.models import UserProfile


class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
    
class UserEdit(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = "registration/edit_settings.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')


def password_success(request):
    return render(request, 'registration/password_success.html', {})

class MyProfilePage(DetailView):
    model = UserProfile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args,**kwargs):
        context = super(MyProfilePage, self).get_context_data(*args, **kwargs)
        my_profile = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["my_profile"] = my_profile
        return context

class ShowProfilePage(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args,**kwargs):
        # user_profile = UserProfile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class EditProfilePage(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile.html'
    fields = ['bio', 'profile_pic', 'web_url', 'fb_url', 'instagram_url', 'linkedin_url', 'whatsapp_url']
    success_url = reverse_lazy('home')

class CreateProfilePage(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'registration/create_profile.html'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)