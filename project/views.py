from django.db import models
from django.shortcuts import redirect, render
from . import models

# Create your views here.

# tampilan awal.
def index(req):
    if req.POST:
        input_nik = req.POST['nik']
        input_password = req.POST['password']
        
        user = models.login.objects.filter(nik=input_nik, password=input_password).first()
        print(user)
        if user is not None:
            return redirect('/home')
    data = models.login.objects.all()
    return render(req, 'login/index.html', {
        'data': data,
    })
        

