import pymongo
from django.test import TestCase

# It would be best to define this in a utility class somewhere
def get_db(db_name=None):
    """ GetDB - simple function to wrap getting a database
    connection from the connection pool.
    """
    return pymongo.Connection(
            host=settings.MONGO_HOST,
            port=settings.MONGO_PORT)[getattr(
                settings, "MONGO_DBNAME_PREFIX", "") +
                (db_name or settings.MONGO_DBNAME)]

class MyTestCase(TestCase):
    fixtures = ['test_data.json']
    def setUp(self):
        self.db = get_db('test')
        self.db.create_collection('mytestcollection')

    def test_doc_published(self):
        # Set up a document to save
        doc = dict(text="test",
                      user_id=1)
        self.db.mytestcollection.save(doc)
        self.assertEqual(self.db.mytestcollection.find_one(
            {'user_id':1})['text'], 'test')

    def tearDown(self):
        self.db.drop_collection('mytestcollection')