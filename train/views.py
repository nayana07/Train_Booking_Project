from django.shortcuts import render,redirect
from .models import train, booking
from .forms import Booking_form
import json, copy

# Create your views here.

def index(request):
    obj=train.objects.all()
    context = {'obj':obj}
    return render(request,'index.html',context)  

def booking(request, book):
    print(book)
    if request.method == 'POST':
      pass
    else:
      myenq = train.objects.get(train_no=book)
      newd1 = copy.copy(myenq.__dict__)
      form = Booking_form(data=newd1, instance=myenq)
      date = newd1['date']
      train_to = newd1['train_to']
      train_from = newd1['train_from']
      train_no = newd1['train_no']
      print(train_from)
      context = {'myenq':myenq, 'form':form, 'date':date, 'train_to':train_to, 'train_no':train_no, 'train_from':train_from}
    return render(request,'booking.html',context)

def booksub(request):
  thank = False
  if request.method == 'POST':
    id = request.POST.get('train_no','')
    print(id)
    form = Booking_form(request.POST)
    if form.is_valid():
      form.save()
      thank = True
    else:
      print(form.errors)
    obj = train.objects.all()   
    form = Booking_form(initial={'t_id':id})
    context = {'form':form , 'obj':obj, 'thank':thank}
    return render(request,'index.html',context)