from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from profiles.mixins import UserAuthenticationMixin
from tasks.forms import TaskCreateForm, TaskUpdateForm, TaskDeleteForm
from tasks.mixins import TaskExistenceMixin
from tasks.models import Task


# Create your views here.

class HomeView(
               UserAuthenticationMixin,
               TaskExistenceMixin,
               ListView
):
    model = Task
    template_name = 'tasks/home-with-profile.html'

    login_message = 'Please log in to view your tasks.'

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


class TaskCreateView(
    UserAuthenticationMixin,
    CreateView
):
    model = Task
    form_class = TaskCreateForm
    # success_url = reverse_lazy('tasks:home')
    success_url = reverse_lazy('tasks:home')
    template_name = 'tasks/task-add.html'

    login_message = 'Please log in to add your tasks.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetailView(UserAuthenticationMixin, DetailView):
    model = Task
    template_name = 'tasks/task-details.html'

class TaskUpdateView(UserAuthenticationMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/task-edit.html'

    def get_success_url(self) -> str:
        return reverse('tasks:detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    form_class = TaskDeleteForm
    template_name = 'tasks/task-delete.html'
    success_url = reverse_lazy('tasks:home')

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)


