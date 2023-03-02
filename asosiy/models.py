from django.db import models
from django.contrib.auth.models import User
class Muallif(models.Model):
    ism=models.CharField(max_length=25)
    tirik=models.BooleanField()
    kitoblar_soni=models.SmallIntegerField()
    jinsi=models.CharField(max_length=10)
    yosh = models.PositiveSmallIntegerField(default=45,null=True)
    def __str__(self):
        return f'{self.ism}'
class Kitob(models.Model):
    nom=models.CharField(max_length=30)     
    sahifa=models.SmallIntegerField()
    mualif_fk=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    janr=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nom}'

class Talaba(models.Model):
    ism=models.CharField(max_length=25)
    bitiruvchi=models.BooleanField()
    kurs=models.SmallIntegerField()
    kitoblar_soni=models.SmallIntegerField(default=0)
    def __str__(self):
        return f'{self.ism}'
    class Meta:
        ordering=('ism',) # tartiblash  uchun


class Admin(models.Model):
    user_fk =models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
    ism=models.CharField(max_length=25)
    ish_vaqti=models.TimeField(null=True,blank=True)
    def __str__(self):
        return f'{self.ism}'

class Record(models.Model):
    talaba_fk=models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob_fk=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    admin_fk=models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana=models.DateTimeField()
    qaytarish_sana=models.DateTimeField()
    qaytarildi=models.BooleanField()






