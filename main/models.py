from django.db import models

class Laptops(models.Model):
    mark = models.CharField('Название', max_length=70)
    describe = models.TextField('Краткое описание')
    RAM = models.IntegerField('Объём RAM')
    SSD = models.FloatField('Объем SSD')
    long_describe = models.TextField('Полное описание')
    

    image = models.ImageField(upload_to='laptops/', verbose_name='Изображение', null=True, blank=True)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.mark
    
    

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
