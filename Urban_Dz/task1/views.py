from django.shortcuts import render
from .forms import UserRegistr
from django.http import HttpResponse
from .models import Game, Buyer

# Create your views here.

def table_users():
    us = Buyer.objects.all()
    users = []
    for user in us:
        users.append(user.name)
    return users

def table_games():
    games = Game.objects.all()
    return games


info = {"error": ''}
def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegistr(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            users = table_users()
            if password1 == password2:
                if int(age) > 17:
                    if name not in users:
                        Buyer.objects.create(name=name, balanse=0, age=age)
                        return HttpResponse(f'Приветствуем {name}', )
                    else:
                        info['error'] = 'Пользователь уже существует'
                        return render(request, "registration_page.html", {'error': info['error'], 'form': form})
                else:
                    info['error'] = 'Вы должны быть старше 18'
                    return render(request, "registration_page.html", {'error': info['error'], 'form': form})
            else:
                info['error'] = "Пароли не совпадают"
                return render(request, "registration_page.html", {'error': info['error'], 'form': form})
        context = {
            'form': form,
            'info': info
        }
        return render(request, "registration_page.html", context)
    else:
        form = UserRegistr()
        context = {
            'form': form,
            'info': info
        }
        return render(request, "registration_page.html", context)


def main_page(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, "main_p.html", context)


def table_of_contents(request):
    title = 'Игры'
    button = 'Купить'
    chapter = table_games()
    context = {
        'title': title,
        'button': button,
        'chapter': chapter
    }
    return render(request, 'table_of_contens.html', context)


def donat(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'donat.html', context)

