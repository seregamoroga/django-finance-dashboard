from django.db import models

class Transaction(models.Model):
    CATEGORY_CHOICES = (
        ('income', 'Доход'),
        ('food', 'Еда'),
        ('subscriptions', 'Подписки'),
        ('other', 'Другое'),
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.amount} ₽ - {self.get_category_display()}"

class Debt(models.Model):
    creditor = models.CharField(max_length=100, default="Мама", verbose_name="Кому должен")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма долга")

    def __str__(self):
        return f"Долг {self.creditor}: {self.amount} ₽"
# Create your models here.
