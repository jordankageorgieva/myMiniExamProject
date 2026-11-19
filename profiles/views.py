from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Model
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView

from profiles.forms import AppUserCreateForm
from profiles.mixins import UserAuthenticationMixin
import logging

from tasks.models import Task

logger = logging.getLogger(__name__)

# Create your views here.
UserModel = get_user_model()


class RegisterAppUserView(CreateView):
    model = UserModel
    form_class = AppUserCreateForm
    template_name = 'profiles/register-page.html'
    success_url = reverse_lazy('profiles:login')

    def form_valid(self, form):
        # 1. Тук взимате речника с почистените и валидни данни от форма
        user_data = form.cleaned_data

        # ВНИМАНИЕ: Паролата обикновено е в 'cleaned_data' като суров низ.
        # Добра практика е да я маснете/скриете от съображения за сигурност!
        logged_data = user_data.copy()
        if "password1" in logged_data:
            logged_data["password1"] = "********"
        if "password2" in logged_data:
            logged_data["password2"] = "********"
        if "password" in logged_data:
            logged_data["password"] = "********"

        # 2. Логвате данните (ще се появят във вашия конзолен изход / лог файл)
        logger.info(f"New user registration attempt with data: {logged_data}")

        # 3. Важно: Винаги извиквайте super().form_valid(form),
        # за да се запише реално обектът в базата данни и да работи success_url редиректът!
        return super().form_valid(form)

# def login_view(request: HttpRequest) -> HttpResponse:
#     return render(request, 'accounts/login-page.html')

class LoginAppUserView(LoginView):
    template_name = 'profiles/login-page.html'

# Create your views here.
# def login_view(request: HttpRequest) -> HttpResponse:
#     profile = get_profile()
# 
#     if profile:
#         # todo add a redirect if a user is logged
#         return redirect('tasks:home')
# 
#     form = ProfileForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('tasks:home')
# 
#     context = {
#         'form': form,
#     }
# 
#     return render(request, 'profiles/home-no-profile.html', context)

class ProfileDetailView(UserAuthenticationMixin, DetailView):
    template_name = 'profiles/profile-details.html'

    login_message = 'Please log in to manage your profile.'

    def get_object(self, queryset=None):
        user = get_user(self.request)
        print(f'The update user is {user}')
        return user

    def get_context_data(self, **kwargs: dict):
        kwargs.update({
            'tasks_count': Task.objects.filter(user=self.object).count() or 0,
            'todo_tasks_count': Task.objects.filter(user=self.object, status="TODO").count() or 0,
        })
        return super().get_context_data(**kwargs)

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('profiles:login')

    def get_object(self, queryset=None):
        user = get_user(self.request)
        print(f'The delete user is {user}')
        return user





