from django.db import models

DEFAULT_STATUS = 'active'
STATUS_CHOICES = (
    (DEFAULT_STATUS, 'Активно'),
    ('blocked', 'Заблокировано'),
)


class GuestBook(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора записи')
    email = models.EmailField(verbose_name='Почта')
    text = models.TextField(max_length=2000, verbose_name='Текст записи')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(max_length=25, default=DEFAULT_STATUS, choices=STATUS_CHOICES, verbose_name='Статус')
    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
