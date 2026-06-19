from django import forms

from .models import ContactEntry


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
