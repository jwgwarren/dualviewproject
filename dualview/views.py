from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.

def home_page(request):
    return render_to_response('home_page.html')

def dual_view(request):
    ctrl = request.GET.getlist('ctrl', None)
    exp = request.GET.getlist('exp', None)
    return render_to_response('dual_view.html',
         {'ctrl':ctrl, 'exp':exp})
    
def main_controls(request):
    return render_to_response('main_controls.html')

def img_controls(request):
    return render_to_response('img_controls.html')