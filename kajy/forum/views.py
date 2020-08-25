from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin #login_required @ view based class
from django.contrib.auth.mixins import UserPassesTestMixin #mano test @ utilisteur
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView,DeleteView
from .models import Post, Commentaire, Vote
from django.contrib import messages 

# Create your views here.

class AboutView(TemplateView):
	template_name = 'forum/about.html'

class HomeView(ListView):
	model = Post
	template_name = 'forum/home.html'
	context_object_name = 'posts'

class ReadPost(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'forum/post_read.html'

class CreatePost(LoginRequiredMixin, CreateView):
	template_name = 'forum/post_create.html'
	#success_url = reverse_lazy('forum_app:home')
	model = Post
	fields =['titre', 'contenu']
		
	def form_valid(self, form):
		form.instance.auteur = self.request.user
		messages.success(self.request, "Création de {} Terminé".format(self.request.POST["titre"]))
		return super().form_valid(form)

class UpdatePost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Post
	fields =['titre', 'contenu']
	template_name = 'forum/post_update.html'
	#success_url = reverse_lazy('forum_app:home')
	def form_valid(self, form):
		"""
			mano ajout automatique ny auteur 
			mianga avy @ ilay utilisateur connecter
		"""
		form.instance.auteur = self.request.user
		messages.success(self.request, "Modification de {} Terminé".format(self.request.POST["titre"]))
		return super().form_valid(form)
		
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.auteur :
			return True
		else:
			return False

class SuprQuestion(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	context_object_name = 'post'
	template_name ='forum/post_delete.html'
	success_url = reverse_lazy('forum_app:home')
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.auteur :
			return True
		else:
			return False
	
			
@login_required
def commenter(request,pk):
	if request.method=='POST':
		text = request.POST['commentaire']
		if len(text)>0 :
			aute=request.user
			coms=request.POST['commentaire']
			quest=Post.objects.get(id=pk)
			c=Commentaire(auteur=aute,contenu=coms,post=quest)
			c.save()
			return redirect("forum_app:read_post",pk)
		else:
			messages.warning(request, "Votre Comentaire est Vide")
			return redirect("forum_app:read_post",pk)
	else:
		return redirect("forum_app:read_post",pk)
		
@login_required
def voter(request, pk):
	if request.method == "GET":
		a = Post.objects.get(pk=pk)
		try :
			v=a.vote_set.get(auteur=request.user.id)
		except Vote.DoesNotExist:
			v=Vote(auteur=request.user,post=a )
			v.save()
		else:
			v.delete()
	return redirect('forum_app:read_post', pk)
