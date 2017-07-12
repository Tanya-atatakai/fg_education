from apps.base_api.parsers import JsonParser
from .exceptions import NotInMutableTagsException


class JsonParserSample_1(JsonParser):
    """Класс для парсера json в html

    Заключает в теги (key) значения атрибутов (value).
    Если какое-то имя атрибута является ключом словаря mutable_tags, то
    вместо имени этого атрибута пишем значение соответствующего ключа
    в mutable_tags
    Если key не соответствует какому-либо ключу из mutable_tags,
    происходит raise исключения NotInMutableTagsException

    """

    mutable_tags = {"title": "h1", "body": "p"}

    def _html_from_dict_json(self, json_data):
        """
        Если ключ key находится в mutable_tags, оборачиваем в тег-значение key
        из mutable_tags значения value, иначе вызываем исключение, что данное
        имя атрибута не подходит.

        :return строку с заключенным в тег-tag значение value | исключение
        :raises: NotInMutableTagsException
        :rtype str
        """
        result = []
        for key, value in json_data.items():
            tag = self.mutable_tags.get(key)
            if tag is None:
                raise NotInMutableTagsException(
                    'Атрибут {key} не подходит для конвертации. Имя атрибута '
                    'может быть только title или body'.format(key=key)
                )
            result.append(
                '<{tag}>{value}</{tag}>'.format(tag=tag, value=value)
            )
        return "".join(result)
