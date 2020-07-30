from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Host(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    host_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,blank=False,default=' ')
    Phone_no = models.IntegerField(default=91)       
    email_id = models.EmailField(max_length=200,default='')
    flat_no = models.IntegerField(default=0)
    no_of_people = models.IntegerField(blank=False,default=0)
    
    host_image = models.ImageField(null=True,blank=True,default='download.jpeg')

    def __str__(self):
        return str(self.name)

class Visitor(models.Model):
    visitor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,blank=False,default='')
    Phone_no = models.CharField(max_length=12,blank=False,default=' ')
    email_id = models.EmailField(max_length=200,blank=False,default='')
    visitor_image = models.ImageField(null=True,blank=True,default='')
    id_proof = models.ImageField(null=True,default='',blank=True)

    def __str__(self):
        return str('Name :')+str(self.name)+str('...Id :')+str(self.visitor_id)+str('...email_id:')+str(self.email_id)


class VisitDetails(models.Model):
    visit_id = models.AutoField(primary_key=True)
    PURPOSE = (
        ('Guest','Guest'),
        ('Home_Service','Home_Service'),
        ('Clients','Clients'),
        ('Delivery_Service','Delivery_Service'),
        ('General_service','General_service'),
        ('Event','Event')
    )
    DURATION = (
        ('1 hours','1 hours'),
        ('5 hours','5 hours'),
        ('1 day','1 day'),
        ('1 week','1 week'),
        ('1 month','1 month'),
        ('5 month','5 month'),
        ('1 year','1 year')
    )
    duration = models.CharField(max_length=20,choices=DURATION)
    purpose = models.CharField(max_length=30,choices=PURPOSE)
    visit_detail = models.ForeignKey(Visitor,null=True, on_delete=models.SET_NULL)
    visit_date = models.DateTimeField(auto_now_add=True)
    flat_no = models.CharField(max_length=300,default=' ')

    def __str__(self):
        return str('Name :')+str(self.visit_detail)+str('------ Id :')+str(self.visit_id)

 
class Event(models.Model):
    EVENT_PURPOSE = (
        ('Birthday','Birthday'),
        ('Meet Up','Meet Up'),
        ('Anniversary','Anniversary'),
        ('Festival','Festival'),
        ('General','General')
    )
    TAG = (
        ('Incomplete','Incomplete'),
        ('Complete','Complete')
    )
    tag = models.CharField(max_length=12,choices=TAG,blank=True,null=True,default='blank')
    event_id = models.AutoField(primary_key=True)
    organizer = models.ForeignKey(Host,null=True, on_delete=models.SET_NULL)
    event_date_time =models.DateTimeField(null=False,unique=True,max_length=20,default='') 
    event_purpose = models.CharField(max_length=12,choices=EVENT_PURPOSE)

    def __str__(self):
        return str(self.organizer)+str('-----') +str(self.event_purpose)



class EventVisitor(models.Model):
    event_visitor_id = models.AutoField(primary_key=True)
    event_info = models.ForeignKey(Event,null=True, on_delete=models.SET_NULL)
    event_visitor_info = models.ForeignKey(Visitor,null=True, on_delete=models.SET_NULL)
    visit_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.event_visitor_info)+str(self.event_visitor_id)


