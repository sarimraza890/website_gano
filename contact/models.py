from django.db import models


class ContactEntry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "contact entry"
        verbose_name_plural = "contact entries"

    def __str__(self):
        return f"{self.name} - {self.email}"
