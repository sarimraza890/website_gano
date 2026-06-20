from django.contrib import admin

from .models import ContactEntry, ReferralEntry


@admin.register(ContactEntry)
class ContactEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("created_at",)


@admin.register(ReferralEntry)
class ReferralEntryAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "referring_dentist", "insurance_name", "created_at")
    search_fields = ("patient_name", "referring_dentist", "insurance_name", "insurance_id")
    readonly_fields = ("created_at",)

