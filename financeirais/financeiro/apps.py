from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class FinanceiroConfig(AppConfig):
    name = 'financeiro'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'