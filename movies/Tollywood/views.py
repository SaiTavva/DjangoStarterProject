from django.shortcuts import render,redirect
from django.http import HttpResponse
from Tollywood.forms import UserForm,TollywoodForm #AddMovie
from django.contrib.auth.decorators import login_required
# from Tollywood.models import Movies
from Tollywood.models import Tollywood



# Create your views here.
def signup(request):
	if request.method=="POST":
		data=UserForm(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse('signup success')
	form=UserForm()
	return render(request,'Tollywood/signup.html',{'form':form})



def home(request):
	return render(request,'Tollywood/home.html')#username passes by default


@login_required #methods visible only on login
def profile(request):
	return render(request,'Tollywood/profile.html')

# @login_required
# def addmovie(request):
# 	if request.method=="POST":
# 		# obj=Movies(movie=request.POST['movie'],hero=request.POST['hero'],heroine=request.POST['heroine'],director=request.POST['director'],producer=request.POST['producer'],description=request.POST['description'])
# 		# obj.save()
# 		form=AddMovie(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect(showmovies)
# 	form=AddMovie()
# 	return render(request,'Tollywood/addmovie.html',{'form':form})

#def showmovies(request):
 #	data=Movies.objects.all()
# 	return render(request,'Tollywood/showmovies.html',{'data':data})

@login_required
def updatemovie(request,id):
 	data=Tollywood.objects.get(id=id)
 	if request.method=="POST":
 		form=TollywoodForm(request.POST,instance=data)
 		if form.is_valid():
 			form.save()
 			return redirect('Tollywoodmovies')
 	form=TollywoodForm(instance=data)
 	return render(request,'Tollywood/updatemovie.html',{'form':form,'data':data})

@login_required
def deletemovie(request,id):
 	data=Tollywood.objects.get(id=id)
 	data.delete()
 	return redirect('Tollywoodmovies')

def addmovie(request):
 	if request.method=="POST":
 		data=TollywoodForm(request.POST,request.FILES)
 		if data.is_valid():
 			data.save()
 			return HttpResponse('data uploaded')

 	form=TollywoodForm()
 	return render(request,'Tollywood/addmovie.html',{'form':form})

def Tollywoodmovies(request):
 	data=Tollywood.objects.all()
 	return render(request,'Tollywood/Tollywoodmovies.html',{'data':data})
