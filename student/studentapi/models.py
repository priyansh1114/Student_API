from django.db import models

# Create your models her
class studenapi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField()
