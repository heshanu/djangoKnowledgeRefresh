#from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})
