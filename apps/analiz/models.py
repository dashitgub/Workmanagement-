from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', default=1)
    
    def clean(self):
        if len(self.name) < 3:
            raise ValidationError('Название задачи должно содержать не менне 3 символов.')

    def __str__(self):
        return self.name


