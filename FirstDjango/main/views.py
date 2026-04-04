from django.shortcuts import render

# Функция для главной страницы - первый этап
def stage1(request):
    """
    Рендерит шаблон 1.html (Первый этап).
    Использует render с путём к шаблону templates/1.html.
    """
    return render(request, '1.html')

# Функция для второго этапа
def stage2(request):
    """
    Рендерит шаблон 2.html (Второй этап).
    Путь к шаблону относительно папки templates.
    """
    return render(request, '2.html')

# Функция для третьего этапа
def stage3(request):
    """
    Рендерит шаблон 3.html (Третий этап).
    """
    return render(request, '3.html')

# Функция для четвёртого этапа
def stage4(request):
    """
    Рендерит шаблон 4.html (Четвертый этап).
    """
    return render(request, '4.html')