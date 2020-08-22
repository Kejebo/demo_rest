from django.db import models
# Create your models here.

class Departament(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=5, unique=True)
    state = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'short_name')
   
    def __str__(self):
        return self.name+' - '+self.short_name

class Skill(models.Model):
    skill = models.CharField('Skill', max_length=50, unique=True)

    def __str__(self):
        return self.skill


class Employee(models.Model):
    jobs = [
        ('0', 'Accountant'),
        ('1', 'Administrator'),
        ('2', 'Economist'),
        ('3', 'Programmer'),
        ('4', 'Others'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job = models.CharField(choices=jobs, max_length=20)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)



    def type_job(self):
      return self.get_job_display()
    

    def __str__(self):
        return self.first_name+' '+' '+self.last_name


    class Meta:
        ordering=['last_name']
        unique_together=('first_name', 'last_name', 'job')
