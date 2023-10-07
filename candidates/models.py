from django.db import models


class Candidate(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)

    resume = models.FileField(upload_to='resumes/')
    linkedin_profile = models.URLField(max_length=200, blank=True, null=True)

    current_job_title = models.CharField(max_length=100, blank=True, null=True)
    current_company = models.CharField(max_length=100, blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
