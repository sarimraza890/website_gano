from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from .models import ReferralEntry
from .forms import ReferralEntryForm


class ReferralTestCase(TestCase):
    def test_referral_model_creation(self):
        referral = ReferralEntry.objects.create(
            patient_name="John Doe",
            date_of_birth=date(1990, 5, 15),
            tooth_numbers="14, 15",
            insurance_name="Delta Dental",
            insurance_id="INS12345",
        )
        self.assertEqual(ReferralEntry.objects.count(), 1)
        self.assertEqual(referral.patient_name, "John Doe")
        self.assertEqual(str(referral), "John Doe - Dentist: N/A")

    def test_referral_form_valid(self):
        data = {
            "patient_name": "Jane Smith",
            "date_of_birth": "1985-10-20",
            "tooth_numbers": "3",
            "insurance_name": "MetLife",
            "insurance_id": "MET9876",
        }
        form = ReferralEntryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_referral_form_invalid(self):
        data = {
            "patient_name": "Jane Smith",
            # Missing date_of_birth, tooth_numbers, insurance_name, insurance_id
        }
        form = ReferralEntryForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("date_of_birth", form.errors)
        self.assertIn("tooth_numbers", form.errors)

    def test_referral_view_get(self):
        response = self.client.get(reverse("referral"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "referral_form.html")
        self.assertIn("form", response.context)

    def test_referral_view_post_success(self):
        # Create a small dummy file to upload
        dummy_file = SimpleUploadedFile("xray.png", b"file_content", content_type="image/png")

        data = {
            "patient_name": "Test Patient",
            "date_of_birth": "2000-01-01",
            "parent_name": "Test Parent",
            "patient_phone": "(502) 555-0199",
            "referring_dentist": "Dr. Test Dentist",
            "dentist_phone": "(502) 555-0299",
            "reason_for_referral": "Consult",
            "tooth_numbers": "19",
            "comments": "Needs evaluation",
            "insurance_name": "Cigna",
            "insurance_id": "CIG-9999",
            "policy_holder": "Test Policy Holder",
            "group_number": "GRP-123",
            "radiograph_1": dummy_file,
        }

        response = self.client.post(reverse("referral"), data=data)
        
        # Check that the form saves and redirects to success state (URL ends with ?sent=1)
        self.assertEqual(response.status_code, 302)
        self.assertIn("sent=1", response.url)

        # Check database entry
        self.assertEqual(ReferralEntry.objects.count(), 1)
        entry = ReferralEntry.objects.first()
        self.assertEqual(entry.patient_name, "Test Patient")
        self.assertIn("xray", entry.radiograph_1.name)
