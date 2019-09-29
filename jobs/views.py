from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'jobs/home.html')#added this lines of code because of the new path created in urls