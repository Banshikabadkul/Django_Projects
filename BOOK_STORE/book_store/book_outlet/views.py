from django.shortcuts import get_object_or_404,render
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
  book = Book.objects.all()
  num_books = book.count()
  avg_rating = book.aggregate(Avg("rating"))
  return render(request,"book_outlet/index.html",{
    "Books":book,
    "total_number_of_books":num_books,
    "average_rating":avg_rating
  })
  
def book_detail(request,id):
  # try:
  #   book = Book.objects.get(slug=slug)
  # except:
  #   raise Http404()
  book = get_object_or_404(Book,pk=id)
  return render(request,"book_outlet/book_detail.html",{
    "title":book.title,
    "author":book.author,
    "rating":book.rating,
    "is_bestseller":book.is_bestselling
      
  })