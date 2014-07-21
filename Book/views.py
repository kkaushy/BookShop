# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.http import HttpResponse





from Book.models import Book


class ListBookView(ListView):
    model = Book
    template_name= 'index.html'
	
def ListCartView(request):
	cart = request.session.get('cart',{})
	
	booklist = Book.objects.filter(id__in = cart.keys())


	return render_to_response('Book/cart.html',{'cart_list':cart,'book_list':booklist})

def add_to_cart(request):
	id = request.POST.get('id')	
	cart = request.session.get('cart',{})	
	cart[id] = int(cart.get(id,0)) + 1
	request.session['cart'] = cart	
	return HttpResponse("ajax call recieved kaushal   dddd")
	
	
