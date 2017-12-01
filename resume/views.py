from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Resume


@login_required
def index(request):
    #TODO: check only 1 is_active==True exists
    if request.user.has_perm('resume.can_view_resume'):

        resume = get_object_or_404(Resume, is_active=True)
        return render(request, 'resume/index.html', {'resume': resume, })
    else:
        return render(request, 'resume/authentication_required.html')
