from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Resume


@login_required
def index(request):
    # TODO: Add is_active field in resume model and get resume base on that
    if request.user.has_perm('resume.can_view_resume'):
        resume = get_object_or_404(Resume, pk=1)
        return render(request, 'resume/index.html', {'resume': resume, })
    else:
        return render(request, 'resume/authentication_required.html')
