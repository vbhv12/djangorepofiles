from django.forms import ModelForm
from .models import *
from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm



def checkforpeople(value):
    if value>5:
        raise forms.ValidationError("residents are more than allowed")

def checkforphone(value):
    if len(str(value))>10 or len(str(value))<10:
        raise forms.ValidationError("Enter valid phone number")


class HostForm(ModelForm):
    no_of_people=forms.IntegerField(validators=[checkforpeople])
    Phone_no=forms.IntegerField(validators=[checkforphone])
    class Meta:
        model = Host
        fields = '__all__'
        exclude = ['user','email_id']



class createuserform(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']



    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count=User.objects.filter(email=email).count()
        if user_count >0:
            raise forms.ValidationError("Enter different email")
        return email




class VisitorForm(ModelForm):
    Phone_no=forms.IntegerField(validators=[checkforphone])
    class Meta:
        model = Visitor
        fields = '__all__'
        exclude = ['user']
        
class VisitDetailsForm(ModelForm):
    class Meta:
        model = VisitDetails
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'

class EventVisitorForm(ModelForm):
    class Meta:
        model = EventVisitor
        fields = '__all__'