from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

def re_name(instance, filename):
	print("maintenant",instance.avatar.path)
	return 'users/avatar/'+str(instance.user.username)+"_"+str(instance.user.id)+"."+filename.split('.')[-1]


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	avatar = models.ImageField(default = 'users/avatar/default.jpg', upload_to = re_name) #'users/avatar/' )
	dateNaissance = models.DateField(blank= True, null = True, verbose_name = 'Date de naissance')
	profession = models.CharField(blank = True, max_length = 50)
	adresse =  models.CharField(blank= True, max_length = 50)
	
	def __str__(self):
		return "{} {}".format(self.user.id, self.user.username)
	
	def get_absolute_url(self):
		return reverse('users_app:profile', kwargs={'pk':self.pk})