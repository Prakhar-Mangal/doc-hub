from django.shortcuts import render
from .models import Disease

# Create your views here.
def home(request):
    return render(request, 'disease/home.html', {'message':''})

def search(request):
    if request.method == 'POST':
        search = request.POST.get('disease')
        print(search)
        disease = Disease.objects.filter(name__iexact=search)
  
        if(disease.count() == 0):
            return render(request, 'disease/home.html', {'message':'We are unable to get this disease'})
        context = { 'disease':disease[0] }
        
        return render(request, 'disease/symptoms.html', context)
    else:
        return render(request, 'disease/home.html', {'message':''})
