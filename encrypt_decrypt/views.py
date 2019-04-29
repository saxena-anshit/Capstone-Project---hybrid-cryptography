from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from .encrypt_file import read_file_enc
from .decrypt_file import read_file_dec

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def dashboard(request):
    return render(request, 'encrypt_decrypt/dashboard.html')


@login_required
def encrypt(request):
    if request.method == 'POST' and request.FILES['text_file']:
        myfile = request.FILES['text_file']

        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)

        text_file_path = os.path.join(BASE_DIR, 'media/' + myfile.name)

        read_file_enc(text_file_path, myfile.name)

        os.remove(text_file_path)

        public_key_path = '/media/' + myfile.name.split('.')[0] + '_public_key.sh'
        enc_file_path = '/media/' + myfile.name + '.sh'

        return render(request, 'encrypt_decrypt/encrypt_file.html', {
            'public_key_path': public_key_path,
            'enc_file_path' : enc_file_path
        })
        
    return render(request, 'encrypt_decrypt/encrypt_file.html')


@login_required
def decrypt(request):

    if request.method == 'POST' and request.FILES['enc_file']:
        myfile = request.FILES['enc_file']

        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        
        file_name = myfile.name
        enc_file_path = os.path.join(BASE_DIR, 'media/' + myfile.name)
        public_key_path = os.path.join(BASE_DIR, 'media/' + myfile.name.split('.')[0] + '_public_key.sh')

        read_file_dec(enc_file_path, public_key_path, file_name)

        os.remove(public_key_path)
        os.remove(enc_file_path)

        decrypted_file_path = '/media/' + myfile.name.split('.')[0] + '.' + myfile.name.split('.')[1]

        return render(request, 'encrypt_decrypt/decrypt_file.html', {
            'uploaded_file_url': decrypted_file_path
        })
        
    return render(request, 'encrypt_decrypt/decrypt_file.html')