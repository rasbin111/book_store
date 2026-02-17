from django.db import models

class CommonModel(models.Model):
    is_deleted = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        
        
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name