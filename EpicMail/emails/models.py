from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=50)
    email_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject