from django.shortcuts import render, redirect
from .models import Transaction, Debt

def dashboard(request):
    # Если пользователь нажал кнопку "Добавить" в форме
    if request.method == 'POST':
        # Забираем данные из формочки
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')
        
        # Создаем новую запись в базе данных
        Transaction.objects.create(
            amount=amount,
            category=category,
            description=description
        )
        # Перезагружаем страницу, чтобы форма очистилась, а данные обновились
        return redirect('dashboard')

    # Обычная загрузка страницы (GET-запрос)
    transactions = Transaction.objects.all().order_by('-date')
    debts = Debt.objects.all()

    context = {
        'transactions': transactions,
        'debts': debts,
    }
    
    return render(request, 'tracker/dashboard.html', context)