from django.db import connection
from django.shortcuts import render,HttpResponse,redirect
from projet.addCvForm import AddCvForm
from django.contrib.auth.models import User
from .models import citoyen,CvCitoyen


# Create your views here.

def Home(request):

    return render(request,'projet/Home.html')


def  AllCv(request):

    #allcv=CvCitoyen.objects.all()

    allcvs=CvCitoyen.objects.select_related('cvCitoyenID')

    users=User.objects.all()
    context={'allcvs':allcvs, 'User':users}
    print(str(allcvs.query))

    return render(request,'projet/allcv.html',context)


def  addCvCitoyen(request):
    current_user = request.user
    if  current_user.id is not None:
        citoyenInfos= citoyen.objects.get(c_UserID=current_user.id)
        fom_cv = AddCvForm(initial={'cvCitoyenID':citoyenInfos.c_ID})
        if request.method=='POST':
            fom_cv=AddCvForm(request.POST,request.FILES)
            if fom_cv.is_valid():
                fom_cv.save()
                return redirect('allcv')

            else:
                print('noooooo')

    else:
        print("user not conected")


    context={'fom_cv':fom_cv}
    return render(request,'projet/addcvcitoyen.html',context)


def VoirProfile(request):
    context={}
    return render(request,'projet/profile.html',context)









def  Home_ID(request,pk):
    return HttpResponse(f"ceci est un {pk} de Home_ID")
