from django.db import models


class TestApiData(models.Model):
    """
    Тестовая модель для фикстуры test_data_sample_#.json
    Содержит входные данные input, эталонные выходные данные output
    и override_settings, показывающий, нужно ли переопределять текущие настройки
    settings_base
    """
    input = models.TextField()
    output = models.TextField()
    override_settings = models.BooleanField(default=False)
