from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator

# Create your models here.
class ApplicationSettings(models.Model):
    id=models.AutoField(primary_key=True)
    module=models.CharField(max_length=50)
    setting_name=models.CharField(unique=True, max_length=50)
    setting_value = models.CharField(max_length=250)
    is_enabled= models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(0) , MaxValueValidator(1)])

    def __str__(self):
        return str(self.id) 