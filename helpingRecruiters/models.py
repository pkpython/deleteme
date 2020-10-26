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