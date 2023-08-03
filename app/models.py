from django.db import models

# Create your models here.
class Trainer(models.Model):
    trainer_name=models.CharField(max_length=100,primary_key=True)
    subject=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.trainer_name
    
    def __str__(self):
        return self.subject