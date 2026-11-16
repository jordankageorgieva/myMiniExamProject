from django import forms

from profiles.models import Profile
from django.contrib.auth import get_user_model

from unfold.forms import UserCreationForm, UserChangeForm


UserModel = get_user_model()

class AppUserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
        }