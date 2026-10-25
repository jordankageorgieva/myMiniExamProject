from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from profiles.forms import ProfileForm
from profiles.models import Profile
from profiles.utils import get_profile
from tasks.mixins import AttachProfileMixin


# Create your views here.
def login_view(request: HttpRequest) -> HttpResponse:
    profile = get_profile()

    if profile:
        # todo add a redirect if a user is logged
        return redirect('tasks:home')

    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tasks:home')

    context = {
        'form': form,
    }

    return render(request, 'profiles/home-no-profile.html', context)

class ProfileUpdateView(AttachProfileMixin, DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs: dict):
        kwargs.update({
            'tasks_count': self.object.tasks.count(),
            'todo_tasks_count': self.object.tasks.filter(status='TODO').count(),
        })
        return super().get_context_data(**kwargs)

class ProfileDeleteView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('profiles:login')

    def get_object(self, queryset=None):
        return get_profile()





