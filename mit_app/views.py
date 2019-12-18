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
        return render(request, "mit_app/mitnadv-detail.html" , {"data":result, "mit":obj})