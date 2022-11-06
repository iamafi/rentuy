from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Profile(models.Model):
    class Genders(models.TextChoices):
        WOMEN = 'Женский'
        MEN = 'Мужской'

    class Role(models.TextChoices):
        LANDLORD = 'Арендодатель'
        CLIENT = 'Клиент'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='пользователь')
    date_of_birth = models.DateField(verbose_name='дата рождения')
    phone_number = models.CharField(max_length=13, verbose_name='номер телефона', default='+998999999999')
    avatar = models.ImageField(upload_to='profiles', blank=True, null=True, verbose_name='фотка',
                               default='profiles/img.png')
    gender = models.CharField(max_length=32, choices=Genders.choices, blank=True, null=True, verbose_name='пол')
    role = models.CharField(max_length=32, choices=Role.choices, verbose_name='роль')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
