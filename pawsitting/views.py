from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse

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
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login

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
@method_decorator(login_required, name='dispatch')
class DetailView(View):
    def get(self, request, id):
        sitter_detail = SitterProfile.objects.annotate(full_name=Concat("user__first_name", Value(" "), "user__last_name"), avg_rating=Avg("user__sit__review__rating")).get(id=id)
        form = BookingForm(sitter=sitter_detail.user)
        return render(request, 'booking_process.html', context={
            'sitter_detail':sitter_detail,
            'form': form
        })
    def post(self, request, id):
        sitter = get_object_or_404(SitterProfile, id=id)
        form = BookingForm(request.POST, sitter=sitter.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.sitter = sitter.user
            booking.status = Booking.StatusChoices.PENDING
            booking.save()
            return redirect('user_booking')
        return render(request, 'booking_process.html', {
            'sitter_detail': sitter,
            'form': form
        })
    
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        profile = SitterProfile.objects.filter(user=request.user).first()
        return render(request, 'user_profile.html', {
            'user': request.user,
            'profile': profile
        })

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/pawsitter/index')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {"form":form})
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login')
        