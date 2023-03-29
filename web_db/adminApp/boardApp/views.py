from django.shortcuts import render
from boardApp.models import user_tbl
from boardApp.models import board_tbl

# Create your views here.
def main(request):
    print(">>>>>>>>>>>>>>>>> main")
    return render(request, 'board/index.html')

def login(request):
    print(">>>>>>>>>>>>>>>>> login")
    id = request.POST['id']
    pwd = request.POST['pwd']

    user = user_tbl.objects.get(user_id = id, user_pwd = pwd)

    request.session['session_name'] = user.user_name
    request.session['session_img'] = user.user_img
    request.session['session_user_id'] = user.user_id
    context = {}
    context['name']= request.session['session_name']
    context['img']= request.session['session_img']
    context['user_id']= request.session['session_user_id']

    return render(request, 'board/main.html', context)

def list(request):
    print(">>>>>>>>>>>>>>>>> list")
    boards = board_tbl.objects.all()
    print(type(boards))

    context ={'boards' : boards}
    context['name'] = request.session['session_name']
    context['img'] = request.session['session_img']
    context['user_id'] = request.session['session_user_id']
    return render(request, 'board/list.html', context)