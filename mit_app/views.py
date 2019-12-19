from django.shortcuts import render

from .models import Mitnadv,Snif

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.http import HttpResponseRedirect, HttpResponse

class MitnadvCreateView(CreateView):
    
    model = Mitnadv
    template_name = "mit_app/mitnadv-create.html"
    fields = [
        "f_name",
        "l_name",
        "gander",
        "age",
        "address",
        "phone",
        "email",
        "image",
        "snif",
        "money_m"]

    context_object_name = "mit"
    

class MitnadvDetailView(DetailView):
    model = Mitnadv
    template_name = "mit_app/mitnadv-detail.html"
    context_object_name = "mit"

    def post(self ,request, **kwargs):

        obj = Mitnadv.objects.get(pk = kwargs["pk"])
        money_for_month = obj.money_for_month
        num = request.POST.get("num-month",0)
        result = int(money_for_month) * int(num)

        money_for_year =int(money_for_month) * 12

        check_boxs = request.POST.getlist("check")

        content = {
            "money_calc":result,
            "money_for_year":money_for_year ,
            "check_boxs" : check_boxs,
            "mit":obj
            }
        #assert False

        return render(request, "mit_app/mitnadv-detail.html" ,content)

    def get(self, request, *args, **kwargs):

        obj = Mitnadv.objects.get(pk = kwargs["pk"])
        money_for_month = obj.money_for_month
        money_for_year =int(money_for_month) * 12

        return render(request, "mit_app/mitnadv-detail.html" , {"money_for_year":money_for_year ,"mit":obj})

class SnifDetailView(DetailView):

    model = Snif
    template_name = "mit_app/snif-detail.html"
    context_object_name = "snif"

    def get(self, request, *args,**kwargs):
        mitnadv = Mitnadv.objects.all()
        snif = Snif.objects.get(pk = kwargs["pk"])

        mit_names = mitnadv.filter(snif = snif)
        content = {
            "mit_names":mit_names,
            "snif":snif,
        }
        #assert False
        return render(request, "mit_app/snif-detail.html", content)
   
