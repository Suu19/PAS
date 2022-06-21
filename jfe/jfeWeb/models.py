from django.db import models

# Create your models here.

class JfeData(models.Model):
    qrcode_data = models.CharField(unique=True, max_length=500)
    kikaku = models.CharField(max_length=100)
    sunpou = models.CharField(max_length=100)
    nagasa = models.CharField(max_length=100)
    honsuu = models.CharField(max_length=100)
    shitsuryou = models.CharField(max_length=100)
    kouhann = models.CharField(max_length=100)
    kessoku_bangou = models.CharField(max_length=100)
    jicqa = models.CharField(max_length=100)
    qa0306011 = models.CharField(max_length=100)
    kikaku_hantei = models.IntegerField()
    sunpou_hantei = models.IntegerField()
    nagasa_hantei = models.IntegerField()
    honsuu_hantei = models.IntegerField()
    kessoku_bangou_hantei = models.IntegerField()
    suuchi_keisan_hantei = models.IntegerField()
    sougou_hantei = models.IntegerField()
    last_update = models.DateField()

    class Meta:
        managed = False
        db_table = 'jfe_data'