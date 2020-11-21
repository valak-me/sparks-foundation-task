from django.db import models
import uuid

# Create your models here.

class customers(models.Model):
    account_number=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name=models.CharField(max_length=50, default=None)
    email=models.EmailField(default=None)
    bal=models.FloatField(default=0)

    def __str__(self):
        return str(self.name)

class transactionhistory(models.Model):
    sender=models.ForeignKey('customers', on_delete=models.CASCADE, related_name='sender')
    receiver=models.ForeignKey('customers', on_delete=models.CASCADE, related_name='receiver')
    amount=models.FloatField()
    result=models.CharField(max_length=50, default='successful')






