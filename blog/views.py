from django.shortcuts import render

# Create your views here.

''' As you can see, we created a method (def) 
called post_list that takes request 
and return a method render that 
will render (put together) our 
template blog/post_list.html. '''

def post_list(request):
	return render(request, 'blog/post_list.html', {})