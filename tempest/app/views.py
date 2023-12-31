from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, forms, login, logout
from django.shortcuts import render
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import FormSubstitua
from django.contrib.auth.decorators import login_required
from .models import Curso, SubstituicaoAula, AceiteSubs


# Create your views here.
def signup_ajax_function(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        fname = request.POST.get('first_name')

        if form.is_valid():
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error_email": "Email already exists"})
            else:
                form.save()
                return JsonResponse({"status": 200})
        else:
            error_name = []
            error_value = []
            for i, j in form.errors.as_data().items():
                print(i, j[0])
                for m in j[0]:
                    error_value.append(m)
                error_name.append(i)

            print(form.errors.as_data())
            error = form.errors.as_data()
            return JsonResponse({"status": "errors", "error_name": error_name, "error_value": error_value})
    else:
        return JsonResponse({"status": "Failed"})


def signin_ajax_function(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            try:
                usr = authenticate(username=username, password=pas)
            except:
                return JsonResponse({'status': 203})
            login(request, usr)
            return JsonResponse({'status': 200})

        else:
            error_name = []
            error_value = []
            for i, j in form.errors.as_data().items():
                print(i, j[0])
                for m in j[0]:
                    error_value.append(m)
                error_name.append(i)

            print(form.errors.as_data())
            error = form.errors.as_data()
            return JsonResponse({"status": "errors", "error_name": error_name, "error_value": error_value})
    else:
        return JsonResponse({"status": "Failed"})


def main(request):
    userCreation = UserCreationForm()
    loginForm = LoginForm()
    return render(request, 'login.html', {'userCreation': userCreation, 'loginForm': loginForm})


def sucesso(request):
    return render(request,'sucesso.html')

@login_required
def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FormSubstitua(request.POST)
            if form.is_valid():
                substituicao_aula = form.save(commit=False)

                # Defina o usuário atual como solicitante
                substituicao_aula.solicitante = request.user

                # Agora, salve a instância do modelo
                substituicao_aula.save()

                return redirect('sucesso')
            else:
                print("ta parando aqui")
        else:
            form = FormSubstitua()

        return render(request, 'home.html', {'form': form})
    else:
        return HttpResponseRedirect('/')


def logoutFun(request):
    logout(request)
    return HttpResponseRedirect('/')

def sobre(request):
    if request.user.is_authenticated:
        return render(request, 'sobre.html')
    else:
        return HttpResponseRedirect('/')



