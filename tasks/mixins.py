from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from profiles.utils import get_profile


class AttachProfileMixin:
    def get_initial(self) -> dict:
        initial = super().get_initial()
        initial['profile'] = get_profile()
        return initial

    def dispatch(self, request, *args, **kwargs):
        profile = get_profile()

        if not profile:
            return redirect('profiles:login')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.profile = get_profile()
        return super().form_valid(form)