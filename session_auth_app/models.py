import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"password reset for {self.user.username} - {self.reset_id}"
