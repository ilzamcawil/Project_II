from django.shortcuts import render

# Create your views here.

# tampilan awal.
def index(req):
    return render(req, 'index.html')
