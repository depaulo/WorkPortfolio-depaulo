from django.shortcuts import render, get_object_or_404
from .models import Job #to let home get the jobs

# Create your views here.
def home(request):
    jobs = Job.objects #passing jobs to home
    return render(request, 'jobs/home.html',{'jobs':jobs})#added this lines of code because of the new path created in urls

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html',{'job':job_detail})#added this lines of code because of the new path created in urls