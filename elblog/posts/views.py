from django.shortcuts import render
from django.views.generic import View
from .models import Post
# Create your views here.
class BaseView(View):
	def get(self,request):
		template_name = "presentacion.html"
		user = request.user 
		return render(request, template_name, {'usuario':user})

class DetailView(View):
	def get(self, request,slug):
		template_name = "detalle.html"
		post = Post.objects.get(slug=slug)
		context = {'post':post}
		return render(request, template_name, context)

class ListView(View):
	"""docstring for ClassName"""
	def get(self, request):
		template_name = 'lista.html'
		posts = Post.objects.all().order_by('-fecha')
		context = {'posts':posts}
		return render(request,template_name, context)
		
