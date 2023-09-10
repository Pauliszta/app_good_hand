from django.shortcuts import render
from django.views import View
from django.db.models import Count
from .models import Donation, Institution
from django.contrib.auth.models import User


# Create your views here.


class LandingPage(View):
    def get(self, request):
        bags_quantities = Donation.objects.all().count()
        institution_quantity = Institution.objects.all().count()
        foundations = Institution.objects.filter(type=1)
        non_gov_organizations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)
        context = {
            "bags": bags_quantities,
            "institutions_quantity": institution_quantity,
            "foundations": foundations,
            "non_gov_organizations": non_gov_organizations,
            "local_collections": local_collections,
        }
        return render(request, "index.html", context=context)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        username = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            user = User.objects.create_user(first_name=name, last_name=surname, username=username, password=password)
            user.save()
            return render(request, "login.html")
    else:
        return render(request, "register.html")

