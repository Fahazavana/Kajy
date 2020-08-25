from django.shortcuts import render, redirect
from django.views.generic import DetailView,TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #login_required @ view based class
from django.contrib.auth.mixins import UserPassesTestMixin #mano test @ utilisteur
from django.contrib import messages 
# Create your views here.

def inscription(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			b=form.save()
			username = form.cleaned_data["username"]
			messages.success(request, "Le compte {} à été cree! vous pouver vous connectez manitenant".format(username))
			#return redirect('forum_app:acceuil_forum')
			return redirect('users_app:connexion')
	else :
		form = UserCreationForm()
	return render(request, 'users/inscription.html', {'form':form})

class SeeProfile(DetailView):
	model = Profile
	template_name =  'users/profile.html'
	
class ChangeInfo(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	template_name = 'users/profile_update.html'
	model = Profile
	fields=["dateNaissance","adresse","profession"]
	
	def form_valid(self, form):
		"""
			mano ajout automatique ny auteur 
			mianga avy @ ilay utilisateur connecter
		"""
		messages.success(self.request, "Modification termine avec succes")
		return super().form_valid(form)
		
	def test_func(self):
		profile = self.get_object()
		if self.request.user == profile.user :
			return True
		else:
			return False
			
class ChangeAvatar(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	template_name = 'users/profile_update.html'
	model = Profile
	fields=["avatar"]
	
	def form_valid(self, form):
		messages.success(self.request, "Avatar changer avaec succèes")
		return super().form_valid(form)
		
	def test_func(self):
		profile = self.get_object()
		if self.request.user == profile.user :
			return True
		else:
			return False

			
class ChangeUser(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	template_name = 'users/profile_update.html'
	model = User
	fields=["username","first_name","last_name","email"]
	success_url = reverse_lazy('forum_app:home')
	def form_valid(self, form):
		"""
			mano ajout automatique ny auteur 
			mianga avy @ ilay utilisateur connecter
		"""
		messages.success(self.request, "Modification termine avec succes")
		return super().form_valid(form)
		
	def test_func(self):
		user = self.get_object()
		if self.request.user == user :
			return True
		else:
			return False
			