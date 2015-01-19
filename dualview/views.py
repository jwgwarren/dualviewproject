from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def home_page(request):
    ctrlImgId = request.GET.getlist('ctrlImgId', None)
    expImgId = request.GET.getlist('expImgId', None)
    return render_to_response('home.html',
         {'ctrlImgId':ctrlImgId, 'expImgId':expImgId})