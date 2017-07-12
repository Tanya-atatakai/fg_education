from html5lib.constants import namespaces
from html5lib.filters.sanitizer import allowed_elements

from apps.base_api.exceptions import NotStrValue


class JsonParser:
    """Класс для парсера json в html

    Заключаем в теги (key) значения атрибутов (value).

    """

    def json_list_to_dict(self, json_data, recursion_depth=0):
        """
        Через все вложенные списки доходит до словаря и
        вызывает _html_from_dict_json

        :param json_data: входные данные json для парсинга
        :param recursion_depth: параметр для ограничения глубины рекурсии
        :type json_data: dict | list
        :type recursion_depth: int
        :return: строку с результатом обхода всех вложенных списков
        либо результат _html_from_dict_json
        :rtype: str
        """
        if recursion_depth > 10:
            return ""

        result = []
        if isinstance(json_data, dict):
            return self._html_from_dict_json(json_data)
        elif isinstance(json_data, list):
            for item in json_data:
                result.append(self.json_list_to_dict(item, recursion_depth+1))

        return "".join(result)

    def _html_from_dict_json(self, json_data):
        """
        Обходит  словарь и оборачивает value в теги key

        :return сгенерированую строку в формате html
        :rtype str
        """
        result = []
        not_html_tags = []
        for key, value in json_data.items():
            if not isinstance(value, str):
                raise NotStrValue('Значением входного атрибута может '
                                  'быть только строка')
            if (namespaces["html"], key) in allowed_elements:
                result.append(
                    '<{tag}>{value}</{tag}>'.format(tag=key, value=value)
                )
            else:
                not_html_tags.append(key)

        if not_html_tags:
            result.append('\n\n<!--Следующие теги не были распарсены, так как '
                          'они не являются тегами html: {tags} -->'.
                          format(tags=", ".join(not_html_tags)))
        return "".join(result)
