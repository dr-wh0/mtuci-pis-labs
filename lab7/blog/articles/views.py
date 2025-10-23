from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                if Article.objects.filter(title=form["title"]).exists():
                    # Проверка на уникальность названия
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        form = {'username': username, 'email': email}
        if not username or not email or not password:  # Проверка на пустые поля
            form['errors'] = "Все поля обязательны для заполнения"
            return render(request, 'register.html', {'form': form})
        if User.objects.filter(username=username).exists():  # Проверка на существующего пользователя
            form['errors'] = "Пользователь с таким логином уже существует"
            return render(request, 'register.html', {'form': form})
        User.objects.create_user(username=username, email=email, password=password)  # Создание пользователя
        return redirect('archive')
    return render(request, 'register.html', {})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        form = {'username': username}
        if not username or not password:  # Проверка на пустые поля
            form['errors'] = "Все поля обязательны для заполнения"
            return render(request, 'login.html', {'form': form})
        user = authenticate(username=username, password=password)  # Аутентификация
        if user is not None:
            login(request, user)  # Авторизация
            return redirect('archive')
        else:
            form['errors'] = "Неверный логин или пароль"
            return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {})
