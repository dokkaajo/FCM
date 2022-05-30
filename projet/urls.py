from django.urls import  path
from  .import views


urlpatterns=[

    path('',views.Home,name='home'),
    path('allcv/',views.AllCv,name='allcv'),
    path('addcvform/', views.addCvCitoyen, name='addcvform'),
    path('voirprofile/',views.VoirProfile,name='voirprofile')


    #path('projet/<str:pk>',views.Home_ID,name='home_id')


]