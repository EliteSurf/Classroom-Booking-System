from django.db import models


class Classroom(models.Model):
    classroom_identity = models.AutoField(primary_key=True)
    classroom_name = models.CharField(max_length=100)
    classroom_capacity = models.IntegerField(null=True)
    classroom_status = models.CharField(max_length=20)

    class Meta:
        db_table = 'table_classroom'
        ordering = ('classroom_identity',)
