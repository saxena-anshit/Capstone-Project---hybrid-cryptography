from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .encrypt_file import read_file

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def dashboard(request):
    return render(request, 'encrypt_decrypt/dashboard.html')


def encrypt(request):
    if request.method == 'POST' and request.FILES['text_file']:
        myfile = request.FILES['text_file']

        text_file_path = os.path.join(BASE_DIR, 'media/text_files/')

        fs = FileSystemStorage(location=text_file_path)
        fs.save(myfile.name, myfile)

        text_file_path = os.path.join(BASE_DIR, 'media/text_files/' + myfile.name)

        read_file(text_file_path, myfile.name)

        return render(request, 'encrypt_decrypt/encrypt_file.html', {
            'uploaded_file_url': text_file_path
        })
        
    return render(request, 'encrypt_decrypt/encrypt_file.html')


def decrypt(request):
    return render(request, 'encrypt_decrypt/decrypt_file.html')