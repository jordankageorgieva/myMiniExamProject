from django.contrib import messages
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class UserAuthenticationMixin(LoginRequiredMixin):
    login_message = 'Please log in to continue.'
    login_url = 'profiles:login'

    def dispatch(self, request, *args, **kwargs):
        user = get_user(self.request)
        print(f"The current user is {user}")
        print(f"The current login message is {self.login_message}")

        if not user or user.is_anonymous:
            messages.warning(request, self.login_message)
            return redirect(self.login_url)

        return super().dispatch(request, *args, **kwargs)