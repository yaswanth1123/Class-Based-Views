from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View,TemplateView

# Create your views here.

# FBV for retuning string
def fbv(request):
    return HttpResponse('This is fbv function')



#CBV for returning string
class Cbv(View):
    def get(self,request):
        return HttpResponse('CBV first view')

#rendering HTML by using Function Based view

def fbv_template(request):
    return render(request,'fbv_template.html')

#rendering HTML by using class based view

class Cbv_template(View):
    def get(self,request):
        d={'name':'yash','age':22}
        return render(request,'Cbv_template.html',d)

#dealing with for in function Bsed view

def fbv_form(request):
    sf=StudentForm()
    d={'sf':sf}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'fbv_form.html',d)

#Dealing with forms in class based View

class Cbv_form(View):
    def get(self,request):
        sf=StudentForm()
        d={'sf':sf}
        return render(request,'Cbv_form.html',d)

    def post(self,request):
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.changed_data))
    
class Cbv_temp(TemplateView):
    template_name='Cbv_template.html'
























