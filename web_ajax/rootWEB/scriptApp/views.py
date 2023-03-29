from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'script/index.html')

def basic(request):
    return render(request, 'script/basic.html')

def dom(request):
    return render(request, 'script/dom.html')

def ajax(request):
    return render(request, 'script/ajax.html')

def maker(request):
    maker = request.POST['maker']
    print('>'*10 ,'param = ', maker)

    response_json = []
    response_json.append({'maker' : maker, 'data': ['A3','A4','A5','A6','A8','RS8']})
    return JsonResponse(response_json, safe=False)