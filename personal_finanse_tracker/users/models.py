from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    default_currency = models.CharField(
        max_length=3,
        choices=[
            ("RUB", "₽ Рубли"),
            ("USD", "$ Доллары"),
            ("EUR", "€ Евро"),
        ],
        default="RUB"
    )

    def str(self):
        return self.username