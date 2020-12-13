from django.db import models


class Website(models.Model):
    """ Model Website """
    url = models.CharField(max_length=150, unique=True)
    ip_address = models.CharField(max_length=150)
    load_time = models.CharField(max_length=150)
    http_code = models.CharField(max_length=150)

    def __str__(self):
        return self.url