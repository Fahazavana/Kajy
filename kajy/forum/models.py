from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import fields
		
class Post(models.Model):
	titre = models.CharField(blank=True, null=True, max_length = 50)
	auteur = models.ForeignKey(User, on_delete = models.CASCADE)
	contenu = models.TextField()
	dateDePublication = models.DateTimeField(auto_now = True, verbose_name = "Date de p*ublication")

	def __str__(self):
		if self.titre:
			return '{} de {}'.format(self.auteur, self.titre)
		else:
			return 'Un post de {}'.format(self.auteur)
		
	def get_absolute_url(self):
		"""
		manome ny url makny @ vue detail ny question iray
		miasa apres creation mba tsy hampiasana success_url
		izay tsy maintsy hampiasan reverse_lazy
		"""
		return reverse("forum_app:read_post", kwargs={'pk':self.pk})
		
		
class Commentaire(models.Model):
	contenu = models.TextField()
	auteur = models.ForeignKey(User, on_delete = models.CASCADE )
	post = models.ForeignKey('Post', on_delete= models.CASCADE)
	datecoms = models.DateTimeField(auto_now = True, verbose_name = "Date de Publication")

	def __str__(self):
		return "{} sur {} ".format(self.auteur, self.post)
		
class Vote(models.Model):
	auteur = models.ForeignKey(User, on_delete = models.CASCADE )
	post = models.ForeignKey('Post', on_delete= models.CASCADE)
	dateVote = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{} {}".format(self.post, self.auteur)
					
