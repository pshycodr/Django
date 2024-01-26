from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def registration(request):
    username = request.POST.get('userName', '') 
    fav_language= request.POST.get('fav_language','')
    
    print(username, fav_language )
    return render(request, 'form.html')



