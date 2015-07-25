from django.shortcuts import render
from django.utils import timezone
from .models import Post
'''Dot after from means current directory or current application. Since views.py and models.py are in the same directory we can simply use . and the 
name of the file (without .py). Then we import the name of the model (Post).'''

# Create your views here.

''' As you can see, we created a method (def) 
called post_list that takes request 
and return a method render that 
will render (put together) our 
template blog/post_list.html. '''

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

