from django.test import TransactionTestCase, Client
from django.test import override_settings
from django.apps import apps

TestApiData = apps.get_model(app_label='base_api', model_name='TestApiData')


class BaseCheck(object):
    test_url = None
    client = Client()

    def _get_response(self, input_data):
        return self.client.post(self.test_url, input_data, 'application/json')

    def _compare_response_with_standard_output(self, response, standard_output):
        if hasattr(self, 'assertEqual'):
            self.assertEqual(response.content.decode('utf-8'), standard_output)

    def test_all_examples(self):
        """
        Обходит все примеры входных данных, сравненивает вернувшийся ответ на
        запрос с эталонными выходными данными.
        Пары входных данных и эталонных выходных находятся в фикстуре
        base_data.json. Проверяются только пары, не требующие переопределения
        каких-либо настроек.
        """
        for test in TestApiData.objects.filter(override_settings=False):
            self._compare_response_with_standard_output(
                self._get_response(test.input), test.output
            )

    @override_settings(JSON_SIZE=5)
    def test_big_size(self):
        """
        Проверяет возврат исключения из-за недостаточного размера входных данных
        Пара вход-эталонный выход в фикстуре base_data.json с pk=1
        """
        big_size_data_pk = 1
        test = TestApiData.objects.get(pk=big_size_data_pk)
        self._compare_response_with_standard_output(
            self._get_response(test.input), test.output
        )

    @override_settings(JSON_LEN=5)
    def test_big_len(self):
        """
        Проверяет возврат исключения из-за недостаточной длины входных данных
        Пара вход-эталонный выход в фикстуре base_data.json с pk=2
        """
        big_len_data_pk = 2
        test = TestApiData.objects.get(pk=big_len_data_pk)
        self._compare_response_with_standard_output(
            self._get_response(test.input), test.output
        )
