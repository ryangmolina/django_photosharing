from django.contrib import auth
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from ..accounts.forms import LoginForm, SignupForm


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('photosharing:home')
    template_name = 'registration/login.html'
    redirect_field_name = auth.REDIRECT_FIELD_NAME

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('photosharing:home')
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(generic.RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SignupView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('photosharing:home')
        return super().get(request, *args, **kwargs)
