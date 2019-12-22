from django.shortcuts import render

from .models import Mitnadv,Snif, Gift

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.http import HttpResponseRedirect, HttpResponse

from django.db.models import Count

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

        def insert_mit_name():
            mitnadv = Mitnadv.objects.all()
            snif = insert_snif()
            mit_names = mitnadv.filter(snif = snif)
            return mit_names

        def insert_snif():
            snif = Snif.objects.get(pk = kwargs["pk"])
            return snif

        def pay_for_all_mitnadvim():
            mitnadvim = insert_mit_name()
            sum = 0 
            for field in mitnadvim.values("money_for_month"):
                sum += int(field["money_for_month"]) 
            return sum
        
        def sum_gift_given():
            mitnadvim = insert_mit_name()
            field_name = "gifts"
            gifts_dic = {}
            sum = 0
            quertset_count = Mitnadv.objects.values(field_name).order_by(field_name).annotate(the_count=Count(field_name))
            for each in quertset_count:
                if each["gifts"] == 1:
                    gift_name = "teeth"
                elif each["gifts"] == 2:
                    gift_name = "vacation"
                elif each["gifts"] == 3:
                    gift_name = "clothes"
                elif each["gifts"] == 4:
                    gift_name = "courses"
                sum += int(each["the_count"])
                
                gifts_dic[gift_name] = each["the_count"]

            return gifts_dic, sum


        mit_names = insert_mit_name()
        snif = insert_snif()

        sum_for_month = pay_for_all_mitnadvim()    
        sum_for_year = sum_for_month * 12

        gifts_dic, sum_gifts = sum_gift_given()

        content = {
            "mit_names":mit_names,
            "sum_for_month":sum_for_month,
            "sum_for_year":sum_for_year,
            "gifts_dic":gifts_dic,
            "sum_gifts":sum_gifts,
            "snif":snif,
        }
        #assert False
        return render(request, "mit_app/snif-detail.html", content)
   

class MitnadviListView(ListView):

    model = Mitnadv
    context_object_name = "all_mit"
    template_name = "mit_app/mitnadvim-list.html"
    
    def get_queryset(self):
        filter_val = self.request.GET.get("filter", "jerusalem-1")
        order = self.request.GET.get("orderby", "f_name")

        new_context = Mitnadv.objects.filter(
            snif__name = filter_val
        ).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "all")
        context["orderby"] = self.request.GET.get("orderby", "f_name")
        return context
    

    def get(self, request, *args, **kwargs):

        obj  = self.get_queryset()
        
        def insert_mit_name():
            mitnadvim = obj
            return mitnadvim
        
        def pay_for_all_mitnadvim():
            mitnadvim = insert_mit_name()
            sum = 0 
            for field in mitnadvim.values("money_for_month"):
                sum += int(field["money_for_month"]) 
            return sum
            
        sum_month = pay_for_all_mitnadvim()
        sum_year = sum_month * 12 
        content = {
            "sum_month":sum_month,
            "sum_year":sum_year,
            "all_mit":obj,
        }
        return render(request, "mit_app/mitnadvim-list.html", content)

