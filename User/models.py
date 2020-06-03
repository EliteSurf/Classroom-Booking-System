from django.db import models
from django.contrib.auth.models import User


# Creating UserAccount Model
class UserProfile(models.Model):
    # One To One Relation Link Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_identity = models.IntegerField(null=False)
    user_phone = models.CharField(max_length=20)
    user_role = models.CharField(max_length=20, default='User')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'table_user_profile'
