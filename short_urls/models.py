from django.db import models

class ShortURL(models.Model):
    alias = models.CharField(primary_key=True, max_length=48)
    long_url = models.URLField(max_length=2048, db_index=True)
