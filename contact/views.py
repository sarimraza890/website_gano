from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactEntryForm, ReferralEntryForm


def meet_the_doc(request):
    return render(request, "meet_the_doc.html")


def services(request):
    form = ContactEntryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(f"{reverse('services')}?sent=1#contact-form")
    return render(request, "services.html", {"form": form, "sent": request.GET.get("sent") == "1"})


def referral_form(request):
    form = ReferralEntryForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(f"{reverse('referral')}?sent=1")
    return render(request, "referral_form.html", {"form": form, "sent": request.GET.get("sent") == "1"})

