from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address',
                  'date_of_birth', 'gender',
                  'resume', 'linkedin_profile',
                  'current_job_title', 'current_company', 'years_of_experience']
