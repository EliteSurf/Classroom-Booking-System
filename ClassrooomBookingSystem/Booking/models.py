from django.db import models
from Classroom.models import Classroom
from User.models import User


# Create your models here.
class Booking(models.Model):
    booking_identity = models.AutoField(primary_key=True)
    booking_classroom_identity = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    booking_user_identity = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.CharField(max_length=20)
    booking_time = models.CharField(max_length=20)
    booking_category = models.CharField(max_length=50)
    booking_reason = models.TextField(blank=True, null=True)
    booking_status = models.CharField(max_length=20, default='Pending')

    class Meta:
        db_table = 'table_booking'
        ordering = ('booking_identity',)