from django.apps import apps
from django.test import TransactionTestCase

from apps.base_api.base_test import BaseCheck

TestApiData = apps.get_model(app_label='base_api', model_name='TestApiData')


class TestSample1(TransactionTestCase, BaseCheck):

    fixtures = ['test_data_sample_1.json']
    test_url = '/sample_1/api'
