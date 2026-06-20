from django import forms

from .models import ContactEntry, ReferralEntry


class ContactEntryForm(forms.ModelForm):
    class Meta:
        model = ContactEntry
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter name"}),
            "email": forms.EmailInput(attrs={"placeholder": "name@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "(502) 240-0649"}),
            "message": forms.Textarea(attrs={"placeholder": "Preferred time or a short question.", "rows": 5}),
        }


class ReferralEntryForm(forms.ModelForm):
    reason_for_referral = forms.ChoiceField(
        choices=ReferralEntry.REASON_CHOICES,
        widget=forms.RadioSelect(),
        required=False
    )

    class Meta:
        model = ReferralEntry
        fields = [
            "patient_name",
            "date_of_birth",
            "parent_name",
            "patient_phone",
            "referring_dentist",
            "dentist_phone",
            "reason_for_referral",
            "tooth_numbers",
            "comments",
            "insurance_name",
            "insurance_id",
            "policy_holder",
            "group_number",
            "radiograph_1",
            "radiograph_2",
            "radiograph_3",
            "radiograph_4",
            "radiograph_5",
        ]
        widgets = {
            "patient_name": forms.TextInput(attrs={"placeholder": "Patient Name"}),
            "date_of_birth": forms.DateInput(attrs={"type": "date", "placeholder": "YYYY-MM-DD"}),
            "parent_name": forms.TextInput(attrs={"placeholder": "Parent Name (if a minor)"}),
            "patient_phone": forms.TextInput(attrs={"placeholder": "(000) 000-0000"}),
            "referring_dentist": forms.TextInput(attrs={"placeholder": "Referring Dentist"}),
            "dentist_phone": forms.TextInput(attrs={"placeholder": "(000) 000-0000"}),
            "tooth_numbers": forms.TextInput(attrs={"placeholder": "Tooth/Teeth Number(s)"}),
            "comments": forms.Textarea(attrs={"placeholder": "Comments...", "rows": 3}),
            "insurance_name": forms.TextInput(attrs={"placeholder": "Insurance Name"}),
            "insurance_id": forms.TextInput(attrs={"placeholder": "Insurance ID#"}),
            "policy_holder": forms.TextInput(attrs={"placeholder": "Policy Holder Name, DOB"}),
            "group_number": forms.TextInput(attrs={"placeholder": "Group #"}),
            "radiograph_1": forms.FileInput(attrs={"accept": ".jpg,.jpeg,.png,.pdf"}),
            "radiograph_2": forms.FileInput(attrs={"accept": ".jpg,.jpeg,.png,.pdf"}),
            "radiograph_3": forms.FileInput(attrs={"accept": ".jpg,.jpeg,.png,.pdf"}),
            "radiograph_4": forms.FileInput(attrs={"accept": ".jpg,.jpeg,.png,.pdf"}),
            "radiograph_5": forms.FileInput(attrs={"accept": ".jpg,.jpeg,.png,.pdf"}),
        }

