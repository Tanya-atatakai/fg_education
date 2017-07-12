
from apps.base_api.parsers import JsonParser


class JsonParserSample_3(JsonParser):
    """Класс для парсера json в html

    Заключает в теги (key) значения атрибутов (value).
    Key должен являться тегом html, иначе он не конвертируется

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
            result.append('<ul>')
            for item in json_data:
                result.append(
                    '<li>' + self.json_list_to_dict(
                        item, recursion_depth + 1) +
                    '</li>'
                )
            result.append('</ul>')

        return "".join(result)
