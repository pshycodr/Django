from django.shortcuts import render

# Create your views here.
def registration(request):
    username = request.POST.get('userName', '') 
    fav_language= request.POST.get('fav_language','')
    
    print(username, fav_language )
    return render(request, 'login_form.html')