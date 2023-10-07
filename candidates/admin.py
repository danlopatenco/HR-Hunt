from django.contrib import admin
from .models import Candidate, JobPosition
from django import forms
from django.contrib.admin import widgets


admin.site.register(JobPosition)


class CandidateAdminForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = '__all__'

    position_fit = forms.ModelMultipleChoiceField(
        queryset=JobPosition.objects.all(),
        widget=widgets.FilteredSelectMultiple('Position Fit', False)
    )


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    form = CandidateAdminForm
    list_display = ('first_name', 'last_name', 'email', 'position_fit_display')

    def position_fit_display(self, obj):
        return ', '.join([position.name for position in obj.position_fit.all()])

    position_fit_display.short_description = 'Position Fit'
