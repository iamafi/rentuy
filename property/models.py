from django.db import models

from account.models import User


class Property(models.Model):
    class District(models.TextChoices):
        ALMAZAR = 'Алмазарский'
        BEKTEMIR = 'Бектемирский'
        MIRABAD = 'Мирабадский'
        MIRZO = 'Мирзо-Улугбекский'
        SERGELI = 'Сергелийский'
        CHILANZAR = 'Чиланзарский'
        SHAYHANTAUR = 'Шайхантаурский'
        YUNUSABAD = 'Юнусабадский'
        YAKKASARAY = 'Яккасарайский'
        YASHNABAD = 'Яшнабадский'
        UCHTEPA = 'Учтепинский'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties', verbose_name='владелец')
    district = models.CharField(max_length=128, choices=District.choices)
    address = models.CharField(max_length=512, verbose_name='адрес')
    floor = models.PositiveIntegerField(verbose_name='этаж')
    max_floor = models.PositiveIntegerField(verbose_name='максимум этажей')
    rooms = models.PositiveIntegerField(verbose_name='количество комнат')
    pets = models.BooleanField(verbose_name='питомцы', default=False)
    for_family = models.BooleanField(verbose_name='для семьи')
    long_term = models.BooleanField(verbose_name='долгосрочный съем')
    total_stars = models.PositiveIntegerField(verbose_name='рейтинг', default=0)
    count_number = models.PositiveIntegerField(verbose_name='количество голосов', default=0)
    verified = models.BooleanField(verbose_name='верифицировано')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def title(self):
        return f'{self.address} {self.rooms}/{self.floor}/{self.max_floor}'

    @property
    def rating(self):
        try:
            return self.total_stars / self.count_number
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'имущество'
        verbose_name_plural = 'имущества'


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/images/')

    def __str__(self):
        return self.property.title


class PropertyVideo(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='properties/videos/')

    def __str__(self):
        return self.property.title
