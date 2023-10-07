from django.urls import path
from .views import (
    list_candidates,
    new_candidate,
    profile_details,
    download_resume
)

urlpatterns = [
    path('list/', list_candidates, name='list_candidates'),
    path('new_candidate', new_candidate, name='new_candidate'),
    path('candidate/<int:id>', profile_details, name='profile_details'),
    path('download_resume/<int:candidate_id>/', download_resume, name='download_resume')

]
