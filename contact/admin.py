import csv
from django.contrib import admin
from django.http import HttpResponse

from .models import ContactEntry, ReferralEntry


def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={meta.model_name}_export.csv"
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = []
        for field in field_names:
            val = getattr(obj, field)
            if hasattr(val, "url"):
                try:
                    row.append(val.url)
                except ValueError:
                    row.append("")
            else:
                row.append(val)
        writer.writerow(row)

    return response


export_as_csv.short_description = "Export Selected to CSV"


@admin.register(ContactEntry)
class ContactEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("created_at",)
    actions = [export_as_csv]


@admin.register(ReferralEntry)
class ReferralEntryAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "referring_dentist", "insurance_name", "created_at")
    search_fields = ("patient_name", "referring_dentist", "insurance_name", "insurance_id")
    readonly_fields = ("created_at",)
    actions = [export_as_csv]

