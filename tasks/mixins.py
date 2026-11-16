from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from profiles.utils import get_profile

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user

from tasks.models import Task


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

class TaskExistenceMixin:

    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if not Task.objects.filter(user=user).exists():
            messages.info(
                request,
                'You have no tasks yet. Please create your first task.'
            )
            return redirect('tasks:create')

        return super().dispatch(request, *args, **kwargs)

