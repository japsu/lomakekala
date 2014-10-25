from django.db import models


class TestFormModel(models.Model):
    foo = models.CharField(max_length=63)
    send_email = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.foo
