from mongoengine import *
from urlshortener.settings import DBNAME

connect(DBNAME)

class Url(Document):

    url_original = URLField(max_length=255, required=True)
    url_modificada = StringField(max_length=56)
    
    def get_absolute_url(self):
        return self.url_original
