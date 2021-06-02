from django.shortcuts import render
from .forms import CsvForm

# Create your views here.

def upload_file_view(request):
    return render(request, 'csvs/upload.html', {})
