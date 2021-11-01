from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from vehicles.models import Van
from django.views import View

# Create your views here.
  

class vehList(TemplateView):
    template_name = 'vehicles/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['van'] = Van.objects.all()
        return context

class vehAdd(View):
    
    def get(self, request):
        return render(request, "vehicles/add.html")
    
    def post(self, request):
        id = request.POST.get('id')
        if(Van.objects.filter(id=id).exists()):
            print("id already taken")
            messages.info(request,"Id already taken")
            return redirect('add')
        company = request.POST.get('company')
        model = request.POST.get('model')
        car = Van.objects.create(id=id, company=company, model=model)
        car.save()
        c = Van.objects.all()
        return render(request, 'vehicles/list.html', {"van": c})

class vehUpdate(View):
    c = Van.objects.all()

    def get(self, request):
        return render(request, "vehicles/update.html",{"van":self.c})
    
    def post(self, request):
        st = request.POST.get('st')
        if(st=='True'):
            id = request.POST.get('id')
            company = request.POST.get('company')
            model = request.POST.get('model')
            speed = request.POST.get('speed')
            avgSpeed = request.POST.get('avgSpeed')
            enStatus = request.POST.get('enStatus')
            flLevel = request.POST.get('flLevel')
            temperature = request.POST.get('temperature')
            if int(flLevel)>100 or int(flLevel)<0:
                f = Van.objects.filter(id=id).first()
                f.company = company
                f.model = model
                f.speed = speed
                f.avgSpeed = avgSpeed
                f.enStatus = enStatus
                f.temperature = temperature
                messages.error(request, "Fuel level must from 0 to 100")
                return render(request, "vehicles/update.html",{"van": f})
            car = Van.objects.filter(id=id).first()
            car.company = company
            car.model = model
            car.speed = speed
            car.avgSpeed = avgSpeed
            car.enStatus = enStatus
            car.flLevel = flLevel
            car.temperature = temperature
            car.save()
            return render(request, 'vehicles/list.html', {"van": self.c})
        else:
            id = request.POST.get('id')
            a = Van.objects.filter(id=id).first()
            return render(request, 'vehicles/update.html',{"van":a})

class vehDel(View):
    def post(self, request):
        id = request.POST.get('id')
        Van.objects.filter(id = id).delete()
        c = Van.objects.all()
        return render(request, "vehicles/list.html",{"van": c})
    

class vehDetail(View):
    def post(self, request):
        id = request.POST.get('id')
        a = Van.objects.filter(id=id).first()
        return render(request, "vehicles/details.html",{"van":a})
    def get(self, request):
        return render(request, "vehicles/details.html",{"van":Van.objects.all().first()})