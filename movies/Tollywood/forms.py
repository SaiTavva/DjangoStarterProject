from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
# from Tollywood.models import Movies
from Tollywood.models import Tollywood

class UserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','password1','password2','email']

# class AddMovie(ModelForm):
#  	class Meta:
#  		model=Movies
#  		fields="__all__"

class TollywoodForm(ModelForm):
	class Meta:
		model=Tollywood
		fields="__all__"