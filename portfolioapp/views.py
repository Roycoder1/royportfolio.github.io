from django.shortcuts import render

from portfolioapp.forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request , 'skills.html')

def projects(request):
    return render(request , 'projects.html')

def contact(request):
    context = {'form': ContactForm}
    if request.method == 'POST':

        date = ContactForm(request.POST)

        if date.is_valid():
            date.save()
            
            
    return render(request, 'contact.html', context)