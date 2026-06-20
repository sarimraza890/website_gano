from django.urls import path

from . import views


urlpatterns = [
    path("", views.meet_the_doc, name="meet_the_doc"),
    path("services/", views.services, name="services"),
    path("referral/", views.referral_form, name="referral"),
]

