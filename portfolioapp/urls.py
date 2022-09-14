from django.contrib import admin
from django.urls import path

from portfolioapp.views import about, contact, home, projects, skills

urlpatterns = [
   path("" , home , name='home'),
    path("about", about,name= 'about' ),
    path("skills", skills,name= 'skills' ),
    path('projects' , projects , name='projects'),
    path('contact', contact , name='contact'),

]
