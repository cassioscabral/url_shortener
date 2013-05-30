#coding: utf-8
from nose.plugins.skip import SkipTest
from shortenerapp.models import Url
from mongoengine.python_support import PY3
from mongoengine import connect
 
try:
    from django.test import TestCase
    from django.conf import settings
except Exception as err:
    if PY3:
        from unittest import TestCase
        # Dummy value so no error
        class settings:
            DBNAME = 'dummy'
    else:
        raise err
 
 
class MongoTestCase(TestCase):
    """
        TestCase class that clear the collection between the tests
    """
    mongodb_name = 'test_%s' % settings.DBNAME
    
    def _pre_setup(self):
        if PY3:
            raise SkipTest('django does not have Python 3 support')
 
        from mongoengine.connection import connect, disconnect
        disconnect()
        connect(self.mongodb_name, port=settings.MONGO_PORT)
        super(MongoTestCase, self)._pre_setup()

    def setUp(self):

        google = Url(url_original="https://www.google.com.br/")
        google.save
        tamanho_maximo_url_reduzida = 11 #5 caracteres da string 'soda/', padrao da url reduzida sao 6 caracteres, no maximo a url deve ter 5 + 6 == 11 caracteres

    def test_numero_de_letras(self):
        self.assertEqual(str.count(google.url_modificada), tamanho_maximo_url_reduzida)
 
    def _post_teardown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.mongodb_name)
        disconnect()
        super(MongoTestCase, self)._post_teardown()