from django.db import models

# Create your models here.
# class Movies(models.Model):
# 	movie=models.CharField(max_length=50)
# 	hero=models.CharField(max_length=20)
# 	heroine=models.CharField(max_length=20)
# 	director=models.CharField(max_length=20)
# 	producer=models.CharField(max_length=20)
# 	description=models.CharField(max_length=100)

class Tollywood(models.Model):
	moviename=models.CharField(max_length=30)
	heroname=models.CharField(max_length=60)
	heroinename=models.CharField(max_length=80)
	director=models.CharField(max_length=50)
	producer=models.CharField(max_length=70)
	cast=models.CharField(max_length=300)
	poster=models.ImageField()