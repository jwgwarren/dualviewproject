from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def dual_view(request):
    ctrlImgId = request.GET.getlist('ctrlImgId', None)
    expImgId = request.GET.getlist('expImgId', None)
    return render_to_response('dual_view.html',
         {'ctrlImgId':ctrlImgId, 'expImgId':expImgId})