import json
from sys import getsizeof
from abc import ABCMeta, abstractmethod

from django.http import JsonResponse
from mezzanine.conf import settings

from .exceptions import JsonValidatorException


class Validator:
    """Базовый класс для проверки валидности входных данных

    Необходимо переопределить метод validate в каждом новом классе
    и добавить имя класса в список validator_classes в функции check_data
    для того, чтобы по нему проходила проверка в функции check_data

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self, check_input):
        pass


class SizeValidator(Validator):
    """Класс для проверки размера входных данных в байтах"""

    # минимум такой, т.к.getsizeof("")=25 байт, а getsizeof(None)=8 байт.
    min_size_of_empty_input = 25

    @classmethod
    def validate(cls, json_input):
        """Ограничение задается в настройках в параметре JSON_SIZE в байтах

        Кроме сравнения с параметром в настройках также проводится проверка
        на то, что размер входных данных <= MIN_SIZE_OF_EMPTY_INPUT байт. 
        Этот параметр задается таким образом, чтобы в случае размера входных 
        данных меньше него выдавалось исключение о пустых входных данных.

        """
        if settings.JSON_SIZE:
            input_size = getsizeof(json_input)
            if input_size <= cls.min_size_of_empty_input:
                raise JsonValidatorException('Пустые входные данные')
            if input_size >= settings.JSON_SIZE:
                raise JsonValidatorException(
                    'Размер входных данных превышает разрешенный на {dif} байт.'
                    ' Максимальный разрешенный размер составляет {standard} '
                    'байт.' .format(
                        dif=(input_size - settings.JSON_SIZE),
                        standard=settings.JSON_SIZE)
                )


class LengthValidator(Validator):
    """ Класс для проверки количества символов входных данных """

    @classmethod
    def validate(cls, json_input):
        """
        Ограничение задается в настройках в параметре JSON_LEN
        в количестве символов
        """
        if settings.JSON_LEN:
            input_len = len(json_input)
            if input_len >= settings.JSON_LEN:
                raise JsonValidatorException(
                    'Длина входных данных превышает разрешенную на {dif} '
                    'символов. Максимальная разрешенная длина составляет '
                    '{standard} символов.'.format(
                        dif=(input_len - settings.JSON_LEN),
                        standard=settings.JSON_LEN)
                )


class JsonValidator(Validator):
    """ Класс для проверки, json ли на входе """

    @classmethod
    def validate(cls, json_input):
        try:
            json.loads(json_input)
        except (ValueError, TypeError):
            raise JsonValidatorException('на входе не json')


def check_data(input_data):
    """Проверка валидности входного JSON

    Все валидаторы наследники класса Validator должны быть добавлены
    в список validator_classes, по которому происходит итерация и
    отлавливаются исключения

    :param input_data: данные, которые будут
    проверяться на валидность
    :type input_data: str
    :return: None либо исключение, которое вернул
    какой-то из валидаторов
    :rtype None| JsonResponse

    """
    # список имен классов валидаторов
    validator_classes = (SizeValidator, LengthValidator, JsonValidator)

    for validator in validator_classes:
        try:
            validator.validate(input_data)
        except JsonValidatorException as error:
            return JsonResponse({'error_detail': error.detail},
                                json_dumps_params={'ensure_ascii': False})
    return None
