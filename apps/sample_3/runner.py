import json
from collections import OrderedDict

from django.http import JsonResponse

from apps.base_api.exceptions import NotStrValue
from apps.base_api.validators import check_data
from apps.sample_3.utils.parsers import JsonParserSample_3


class Runner:
    """
    Класс для запуска конвертера с предварительной валидацией данных
    """
    @classmethod
    def convert_json2html(cls, input_data):
        """Конвертирует json в html

        Сначала проверяем входные данные валидаторами на наличие ошибки.
        если validator_error is not None, значит входной JSON не валиден,
        возвращаем эту ошибку.
        Если не было return, тогда входные данные парсятся в удобный для
        перебора тип, а затем идет конвертация в html с оборачиванием значений
        атриутов json в теги-атрибуты.

        :param input_data: данные, которые будут обрабатываться парсером
        :type input_data: str
        :return: ошибку валидации либо сконвертированные данные в result
        :raises: NotInMutableTagsException, JsonValidatorException
        :rtype: JsonResponse | str

        """
        validator_error = check_data(input_data)
        if validator_error is not None:
            return validator_error
        loads_input = json.loads(input_data, object_pairs_hook=OrderedDict)
        parsed_input = JsonParserSample_3()
        try:
            result = parsed_input.json_list_to_dict(loads_input)
        except NotStrValue as error:
            return JsonResponse({'error_detail': error.detail},
                                json_dumps_params={'ensure_ascii': False})
        return result
