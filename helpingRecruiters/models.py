from django.db import models

# Create your models here.
class newJob(models.Model):
    jobtitle = models.CharField(max_length = 100)
    CompanyName = models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
    jDesc = models.CharField(max_length = 100)
    resp = models.CharField(max_length = 100)
    salaryDesc = models.CharField(max_length = 100)

    def __str__(self):
        return self.jobtitle

class applied(models.Model):
    job = models.ForeignKey(newJob, on_delete = models.CASCADE)
    candidateName = models.CharField(max_length = 250)
    address = models.CharField(max_length = 1500)
    highestQual = models.CharField(max_length = 200)
    skills = models.CharField(max_length = 1500)
    contact = models.CharField(max_length = 13)
    
    def __str__(self):
        return self.candidateName