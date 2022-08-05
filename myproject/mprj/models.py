from django.db import models

#Burada modelimizi, neslerimizi özellikleriyle tanımlıyoruz.
#Bizim formumuzda 4 değişken var bunların özellikleriyle beraber ekliyoruz.

class Contact(models.Model):
      name = models.CharField(max_length=15)
      email= models.EmailField()
      message = models.TextField()

      SUBJECT = [
            ('SL', 'Sales'),
            ('BY', 'Buying'),
            ('MG', 'Management'),
            ('BG', 'Budget')
      ]

      sub = models.CharField(max_length=2, choices=SUBJECT, default=SUBJECT[3][0])
