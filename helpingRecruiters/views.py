from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
import time
# Create your views here.
def home(request):
    if request.method == 'POST':
        user_id = request.POST.get('userID')
        password = request.POST.get('password')
        if(user_id=="recruiter@abc.com"):
            jobs = models.newJob.objects.all()
            print("is a recruiter")
            return render(request, "helpingRecruiters/recruiter.html" , {"jobs":jobs})
        
        elif(user_id == "candidate@abc.com"):
            jobs = models.newJob.objects.all()
            print("is a consumer")
            return render(request, "helpingRecruiters/candidateview.html" , {"jobs":jobs})
        
        else:
            print("not authenticated")


    return render(request, 'helpingRecruiters/login.html')

def recruiterlist(request):
    jobs = models.newJob.objects.all()
    return render(request, "helpingRecruiters/recruiter.html" , {"jobs":jobs})

def addNew(request):
    if request.method == "POST":
        _jobtitle = request.POST.get('Jobtitle')
        _CompanyName = request.POST.get('CompanyName')
        _Location = request.POST.get('Location')
        _jDesc = request.POST.get('jDesc')
        _resp = request.POST.get('resp')
        _salaryDesc = request.POST.get('sDesc')
        print(request.POST)
        print(_CompanyName," ", _Location, " ", _jDesc, " ", _resp, " ", _salaryDesc)
        # time.sleep(100000)
        instance = models.newJob(jobtitle= _jobtitle, CompanyName=_CompanyName, Location=_Location, jDesc=_jDesc, resp=_resp, salaryDesc=_salaryDesc,)
        instance.save()
        return redirect("helpingRecruiters-recruiterlist")
    return render(request, 'helpingRecruiters/postjob.html')

def jobdetail(request, pk):
    job = models.newJob.objects.get(pk = pk )
    return render(request, "helpingRecruiters/jobdetail.html", {"job":job})


def jobupdate(request, pk):
    job = models.newJob.objects.get(pk = pk )
    if request.method == "POST":
        _jobtitle = request.POST.get('Jobtitle')
        _CompanyName = request.POST.get('CompanyName')
        _Location = request.POST.get('Location')
        _jDesc = request.POST.get('jDesc')
        _resp = request.POST.get('resp')
        _salaryDesc = request.POST.get('sDesc')
        job.jobtitle= _jobtitle
        job.CompanyName=_CompanyName
        job.Location=_Location
        job.jDesc=_jDesc
        job.resp=_resp
        job.salaryDesc=_salaryDesc
        job.save()
        return redirect("helpingRecruiters-recruiterlist")

    return render(request, "helpingRecruiters/jobUpdate.html", {"job":job})

def jobdeleteconfirm(request, pk):
    job = models.newJob.objects.get(pk = pk )    
    return render(request, "helpingRecruiters/jobdelete.html", {"job":job})

def jobdelete(request, pk):
    job = models.newJob.objects.get(pk = pk )
    job.delete()
    return redirect('helpingRecruiters-recruiterlist')
    
def applynow(request, pk):
    jobdetail = models.newJob.objects.get(pk = pk )
    jobs = models.newJob.objects.all()

    if request.method == "POST":
        jobName = jobdetail
        _candidateName = request.POST.get("CName")
        _address = request.POST.get("address")
        _highestQual = request.POST.get("Qual")
        _skills = request.POST.get("skills")
        _contact = request.POST.get("contact")
        instance = models.applied.objects.create(job = jobName, candidateName=_candidateName , address=_address , highestQual=_highestQual , skills=_skills , contact=_contact )
        instance.save()
        return render(request, "helpingRecruiters/candidateview.html" , {"jobs":jobs})

    return render(request, "helpingRecruiters/applyjob.html", {"job":jobdetail})
