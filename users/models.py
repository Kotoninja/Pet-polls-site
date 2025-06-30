from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    """
    Attributes:
    user : str
        connects user with User database
    count_created_of_polls : int
        count of created polls by user
    count_answered_of_polls : int
        number of polls answered by user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count_created_of_polls = models.IntegerField(default=0)
    count_answered_of_polls = models.IntegerField(default=0)
