from django import forms

from tasks.models import Task


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Task Title'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description'}
            ),
            'status': forms.Select(
                attrs={'placeholder': 'Task Status'}
            ),
            'created_at': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'placeholder': 'Task Creation date'}
            ),
            'due_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'placeholder': 'Task Due date',
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].empty_label = 'Select a category'
        self.fields['category'].help_text = (
            'Adding a category helps you organize and manage your tasks more effectively.'
        )
        self.fields['category'].required = False


class TaskCreateForm(TaskBaseForm):
    ...


class TaskUpdateForm(TaskBaseForm):
    ...


class TaskDeleteForm(TaskBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
