from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    species = models.CharField(max_length=100, verbose_name='Вид')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    health = models.CharField(
        max_length=20,
        choices=[
            ('отличное', 'Отличное'),
            ('хорошее', 'Хорошее'),
            ('удовлетворительное', 'Удовлетворительное'),
            ('плохое', 'Плохое'),
        ],
        verbose_name='Здоровье'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name
