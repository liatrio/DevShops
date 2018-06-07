from django.shortcuts import render

from .models import List

def home(request):
    my_list = List.objects.order_by('id')

    context = {'my_list' : my_list}
    
    template = 'home.html'
    return render(request, template, context)
