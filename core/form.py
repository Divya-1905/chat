from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User

from core.models import messagemodel
class signup(ModelForm):
   class Meta:
       model=User
       fields = ['username','password','email']
class login(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']  
class message(ModelForm):
    class Meta:
        model: messagemodel
        fields = '__all__'        
             
       