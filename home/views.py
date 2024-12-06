from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request, 'home/index.html')
    paginate_by = 6