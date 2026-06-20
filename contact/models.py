from django.db import models


class ContactEntry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "contact entry"
        verbose_name_plural = "contact entries"

    def __str__(self):
        return f"{self.name} - {self.email}"


class ReferralEntry(models.Model):
    REASON_CHOICES = [
        ("Consult", "Consult"),
        ("Root Canal Treatment", "Root Canal Treatment"),
        ("Retreatment", "Retreatment"),
    ]

    # Patient Information
    patient_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()
    parent_name = models.CharField(max_length=120, blank=True, null=True)
    patient_phone = models.CharField(max_length=40, blank=True, null=True)

    # Dentist Information
    referring_dentist = models.CharField(max_length=120, blank=True, null=True)
    dentist_phone = models.CharField(max_length=40, blank=True, null=True)

    # Referral Details
    reason_for_referral = models.CharField(max_length=50, choices=REASON_CHOICES, blank=True, null=True)
    tooth_numbers = models.CharField(max_length=120)
    comments = models.TextField(blank=True, null=True)

    # Insurance Information
    insurance_name = models.CharField(max_length=120)
    insurance_id = models.CharField(max_length=120)
    policy_holder = models.CharField(max_length=120, blank=True, null=True)
    group_number = models.CharField(max_length=120, blank=True, null=True)

    # Radiographs (up to 5 uploads)
    radiograph_1 = models.FileField(upload_to="radiographs/", blank=True, null=True)
    radiograph_2 = models.FileField(upload_to="radiographs/", blank=True, null=True)
    radiograph_3 = models.FileField(upload_to="radiographs/", blank=True, null=True)
    radiograph_4 = models.FileField(upload_to="radiographs/", blank=True, null=True)
    radiograph_5 = models.FileField(upload_to="radiographs/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "referral entry"
        verbose_name_plural = "referral entries"

    def __str__(self):
        return f"{self.patient_name} - Dentist: {self.referring_dentist or 'N/A'}"

