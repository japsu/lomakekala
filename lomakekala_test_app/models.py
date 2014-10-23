from django.db import models


class TestFormModel(models.Model):
    foo = models.CharField(max_length=63)

    def __unicode__(self):
        return self.foo
