from django.db import models

# Create your models here.
class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TODO = "TODO", "To do"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        DONE = "DONE", "Done"

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    profile = models.ForeignKey(
        to = 'profiles.Profile',
        on_delete = models.CASCADE,
        related_name = "tasks",
        # null=True,
        # blank=True,
    )

    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
