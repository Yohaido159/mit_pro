from django.shortcuts import render

from .models import Mitnadv,Snif, Gift

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from django.http import HttpResponseRedirect, HttpResponse

from django.db.models import Count

from django.urls import reverse_lazy

from django.core.mail import send_mail



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
        "time_start",
        "time_end",
        "gifts",
        "money_for_month"]

    context_object_name = "mit"
    
    def get_success_url(self):
        return reverse_lazy("mitnadv-detail", kwargs={"pk" : self.object.pk})


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

        return render(request, "mit_app/mitnadv-detail.html" ,content)

    def get(self, request, *args, **kwargs):

        def get_next_mit():
            next = Mitnadv.objects.filter(pk__gt = kwargs["pk"]).order_by("pk").first()
            return next

        def get_pre_mit():
            pre = Mitnadv.objects.filter(pk__lt = kwargs["pk"]).order_by("pk").last()
            return pre

        next_mit = get_next_mit()
        pre_mit = get_pre_mit()


        obj = Mitnadv.objects.get(pk = kwargs["pk"])
        money_for_month = obj.money_for_month
        money_for_year =int(money_for_month) * 12
        
        content = {
            "money_for_year":money_for_year,
            "next_mit":next_mit,
            "pre_mit":pre_mit,
            "mit":obj,
        }

        return render(request, "mit_app/mitnadv-detail.html" , content)


class MitnadviListView(ListView):

    model = Mitnadv
    context_object_name = "all_mit"
    template_name = "mit_app/mitnadvim-list.html"
    snifs = Snif.objects.all()

    def get_queryset(self):
        filter_val = self.request.GET.get("filter", "all")
        order = self.request.GET.get("orderby", "f_name")
        if filter_val == "all":
            return Mitnadv.objects.all()
        else:
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
            "snifs":self.snifs,
            "all_mit":obj,
        }
        
        return render(request, "mit_app/mitnadvim-list.html", content)



class SnifCreateView(CreateView):
    
    model = Snif
    template_name = "mit_app/snif-create.html"
    fields = [
        "name",
        "address",
        "image",
    ]

    context_object_name = "snif"
    
    def get_success_url(self):
        return reverse_lazy("snif-detail", kwargs={"pk" : self.object.pk})


class SnifDetailView(DetailView):

    model = Snif
    template_name = "mit_app/snif-detail.html"
    context_object_name = "snif"

    def post(self, request, *args, **kwargs):

        

        def insert_mit_name():
            mitnadv = Mitnadv.objects.all()
            snif = insert_snif()
            mit_names = mitnadv.filter(snif = snif)
            return mit_names

        def insert_snif():
            snif = Snif.objects.get(pk = kwargs["pk"])
            return snif

        def get_list_mail_to_mitnadvim():
            list_mit_mail = []
            mits = insert_mit_name()
            for mit in mits:
                mail = mit.email
                list_mit_mail.append(mail)
            return list_mit_mail

        list_mail_to_mits = get_list_mail_to_mitnadvim()
        snif = insert_snif()
        subject = self.request.POST.get("subject" , 0)
        message = self.request.POST.get("message" , 0)
        if message == "":
            message = "default - nothing to see here, hi mayan :) send from django"

        #send_mail(
        #    subject,
        #    massage,
        #    "yohaido159@gmail.com",
        #    list_mail_to_mits
        #)





        content = {
            "snif":snif,
        }

        return render(request, "mit_app/snif-detail.html", content)


        

        

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
            quertset_count = mitnadvim.values(field_name).order_by(field_name).annotate(the_count=Count(field_name))

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


        def get_next_snif():
            next = Snif.objects.filter(pk__gt = kwargs["pk"]).order_by("pk").first()
            return next

        def get_pre_snif():
            pre = Snif.objects.filter(pk__lt = kwargs["pk"]).order_by("pk").last()
            return pre



        next_snif = get_next_snif()
        pre_snif = get_pre_snif()

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
            "pre_snif":pre_snif,
            "next_snif":next_snif,
            "snif":snif,
        }
        return render(request, "mit_app/snif-detail.html", content)
   

class SnifListView(ListView):

    model = Snif
    context_object_name = "all_snifs"
    template_name = "mit_app/snifs-list.html"

    snifs = Snif.objects.all()


    def get_queryset(self):
        filter_val = self.request.GET.get("filter", "all")
        order = self.request.GET.get("orderby", "name")

        if filter_val == "all":
            return Snif.objects.all()
        else:
            new_context = Snif.objects.filter(
                name = filter_val
            ).order_by(order)
            return new_context
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "all")
        context["orderby"] = self.request.GET.get("orderby", "name")
        return context
    

    def get(self, request, *args, **kwargs):
        

        def mitnadvim_in_snif():
            snifs = Snif.objects.all()
            mit_dict = {}

            for snif in snifs:
                mits = snif.mitnadv_set.all()
                mit_dict[snif.name] = mits
            return mit_dict
        
        mit_dict = mitnadvim_in_snif()

        obj  = self.get_queryset()
        
        content = {
            "snifs":self.snifs,
            "mit_dict":mit_dict,
            "all_snifs":obj,
        }
        
        return render(request, "mit_app/snifs-list.html", content)


