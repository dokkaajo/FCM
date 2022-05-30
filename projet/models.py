from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class  citoyen(models.Model):
  c_ID =models.AutoField(primary_key=True)
  c_UserID = models.ForeignKey(User, on_delete=models.CASCADE)
  c_Residence=models.CharField(max_length=200,blank=True,null=True)
  c_Nationalite=models.CharField(max_length=200,blank=True,null=True)
  c_Image=models.FileField(upload_to='ImageProfile/',blank=True,null=True)



class  CvCitoyen(models.Model):
  cvID = models.AutoField(primary_key=True)
  cvCitoyenID=models.ForeignKey(citoyen, on_delete=models.CASCADE)
  cvTitre=models.CharField(max_length=200,blank=True,null=True)
  cvNiveauEtude=models.CharField(max_length=200,blank=True,null=True)
  GRADES_CHOICES = [
    ('Expert', 'Expert'),
    ('Sen', 'Senior'),
    ('inter', 'Intermédiaire'),
    ('deb', 'Débutant'),
  ]
  cvGrade=models.CharField(max_length=200,choices=GRADES_CHOICES)
  cvResume= RichTextField()
  cvCitoyenPdf=models.FileField(upload_to='cvPdfProfile/',blank=True,null=True)

  def __str__(self):
    return self.cvTitre


