from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import chatroom
from django.contrib.auth.models import User

from core.models import messagemodel
class signup(ModelForm):
    class Meta:
       model=User
       fields = ['username','password','email']
    def save(self, commit=True):                                       
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            print(user)
            user.save()
            return user
class loginform(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']  
class messageform(ModelForm):
    class Meta:
        model = messagemodel
        fields = '__all__'        
class roomform(ModelForm):
    class Meta:
        model = chatroom
        fields = '__all__'
                            