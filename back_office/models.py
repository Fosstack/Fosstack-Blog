from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email
