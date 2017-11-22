from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Resume
from .models import Skill


def index(request):
    resume = get_object_or_404(Resume, pk=1)
    return render(request, 'resume/index.html', {'resume': resume, })


def resume_view(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume/index.html', {'resume': resume})
