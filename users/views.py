from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'registration/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email,  password=password)
        user.save()


        return HttpResponse('Usuário cadastrado com sucesso!')
    
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html' )
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

    if user == 'None':
        return HttpResponse('Email ou Senha invalidos')
