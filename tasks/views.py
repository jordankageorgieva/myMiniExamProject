from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from profiles.utils import get_profile
from tasks.forms import TaskCreateForm, TaskUpdateForm, TaskDeleteForm
from tasks.mixins import AttachProfileMixin
from tasks.models import Task


# Create your views here.

class HomeView(ListView):
    model = Task
    template_name = 'tasks/home-with-profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not get_profile():
             return redirect('profiles:login')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        selected_status = self.request.GET.get('status', '')

        if selected_status in Task.StatusChoices.values:
            queryset = queryset.filter(status=selected_status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Task.StatusChoices.choices
        context['selected_status'] = self.request.GET.get('status', '')
        return context


class TaskCreateView(AttachProfileMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks:home')
    template_name = 'tasks/task-add.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task-details.html'

    def dispatch(self, request, *args, **kwargs):
        if not get_profile():
            return redirect('profiles:login')
        return super().dispatch(request, *args, **kwargs)

class TaskUpdateView(AttachProfileMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/task-edit.html'

    def get_success_url(self) -> str:
        return reverse('tasks:detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    form_class = TaskDeleteForm
    template_name = 'tasks/task-delete.html'
    success_url = reverse_lazy('tasks:home')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)


