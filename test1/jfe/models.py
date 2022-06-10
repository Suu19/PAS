from django.db import models

# Create your models here.
class Pushtodatabase(models.Model):
    image_id = models.IntegerField(primary_key=True)
    image_path = models.CharField(max_length=255)
    jis_result = models.CharField(max_length=50)
    qr_result = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pushtodatabase'