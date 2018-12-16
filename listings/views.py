from django.shortcuts import render

# Create your views here.
def index(request):
    render(request, 'listings/listings.html ')

def listing(request):
    render(request, 'listings/listing.html ')

def search(request):
    render(request, 'listings/search.html ')