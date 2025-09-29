from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import *
from django.views import View
from pawsitting.models import *
from django.db.models import *
from django.db.models.functions import  *
from pawsitting.forms import *
from django.db import transaction

class IndexView(View):
    def get(self, request):
        search_txt = request.GET.get("search", "")
        filter_type = request.GET.get("filter", "name")

        filters = {}
        if search_txt:
            if filter_type == "name":
                filters["full_name__icontains"] = search_txt
            elif filter_type == "service":
                filters["service__name__icontains"] = search_txt
            elif filter_type == "address":
                filters["user__address__icontains"] = search_txt
            elif filter_type == "rating":
                filters["avg_rating"] = search_txt

        sitter_list = SitterProfile.objects.annotate(full_name=Concat("user__first_name", Value(" "), "user__last_name"), avg_rating=Avg("user__sit__review__rating")).filter(**filters)

        return render(request, "find_sitter.html", context={
            "total": sitter_list.count(),
            "sitter_list": sitter_list,
            "filter": filter_type,
            "search": search_txt
        })

class DetailView(View):
    def get(self, request, id):
        sitter_detail = SitterProfile.objects.annotate(full_name=Concat("user__first_name", Value(" "), "user__last_name"), avg_rating=Avg("user__sit__review__rating")).get(id=id)
        return render(request, 'booking_process.html', context={
            'sitter_detail':sitter_detail
        })

    
