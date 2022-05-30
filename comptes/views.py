from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from comptes.userForm import  InscriptionUserForm
from comptes.citoyenForm import CitoyenForm
from django.contrib.auth.models import User
# Create your views here.

def Inscription(request):


     form = InscriptionUserForm()
     if request.method=='POST':
          form = InscriptionUserForm(request.POST)

          if form.is_valid():
               pw =form.cleaned_data["password1"]
               pw_confirmed= form.cleaned_data["password2"]
               if pw==pw_confirmed:
                    #créer un user u
                    logout(request)
                    u=User.objects.create_user(username=form.cleaned_data["username"],first_name=form.cleaned_data["first_name"] ,last_name=form.cleaned_data["last_name"],email=form.cleaned_data["email"], password=pw)
                    if u is not None:
                         u.save()

                         login(request,u)
                         return redirect('addCitoyen')

          else:
                print('Erreur au niveau du formulaire')

     context = {'form': form}
     return render(request,'comptes/inscription.html',context)


def CreateCitoyen(request):
     msgError=""
     if request.user is not None:
          current_user = request.user
          formcitoyen=CitoyenForm(initial={'c_UserID':current_user.id })

          if request.method=='POST':

               formcitoyen = CitoyenForm(request.POST,request.FILES)

               if formcitoyen.is_valid():

                    formcitoyen.save()
                    return redirect('addcvform')
               else:
                     msgError="Oups!,les formulaire non valide"


     else:
           msgError="L'utilisateur doit être connecté !"

     context={'formcitoyen':formcitoyen,'msgError':msgError}
     return render(request,'comptes/addcitoyen.html',context)
