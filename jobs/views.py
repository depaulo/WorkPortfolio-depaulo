from django.shortcuts import render
from .models import Job #to let home get the jobs

# Create your views here.
def home(request):
    jobs = Job.objects #passing jobs to home
    return render(request, 'jobs/home.html',{'jobs':jobs})#added this lines of code because of the new path created in urls

