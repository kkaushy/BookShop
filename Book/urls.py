from django.conf.urls import patterns, include, url

import Book.views

urlpatterns = patterns('',
    url(r'^$', Book.views.ListBookView.as_view(),name='book-list'),
	url(r'^list_cart$', Book.views.ListCartView,name='list-cart'),
	url(r'^add_to_cart$', Book.views.add_to_cart,name='ajax'),	
	url(r'^login$', Book.views.loginView,name='login'),	
)