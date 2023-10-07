from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404


from .models import Candidate
from .forms import CandidateForm


@login_required
def list_candidates(request):

    candidates = Candidate.objects.all()

    context = {
        'link_active': 'list_candidates',
        'candidates': candidates
    }
    return render(request, 'list.html', context)


@login_required
def new_candidate(request):
    context = {
        'link_active': 'list_candidates',
        'form': CandidateForm
    }
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_candidates')
        else:
            print('Form is not valid', form.errors)
            return render(request, 'new_candidate.html', context)

    return render(request, 'new_candidate.html', context)


@login_required
def profile_details(request, id):

    candidate_object = Candidate.objects.get(pk=id)
    print('CANDIDATE', candidate_object.id)
    context = {
        'link_active': 'list_candidates',
        'profile': candidate_object
    }

    return render(request, 'candidate_details.html', context)


@login_required
def download_resume(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    resume_file = candidate.resume.path
    response = FileResponse(open(resume_file, 'rb'))
    response['Content-Disposition'] = f'attachment; filename={candidate.resume.name}'
    return response
