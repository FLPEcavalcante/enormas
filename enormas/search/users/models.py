import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class DataModel(models.Model):
    """A model representing data stored in a specific URL.

    Args:
        models (module): Django's database models module.

    Attributes:
        url (models.URLField): The URL for which the data is stored.
        content (models.JSONField): The data stored in JSON format.
        created_at (models.DateTimeField): The date and time when the data was stored.

    Returns: None
    """
    url = models.URLField()
    content = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        """Meta class for DataModel model."""
        app_label = 'search'
        verbose_name = 'Data Model'

    def __str__(self):
        """DataModel model data url representation."""
        return self.url
