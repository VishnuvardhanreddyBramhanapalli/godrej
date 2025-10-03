from django.db import models

# Create your models here.
class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
