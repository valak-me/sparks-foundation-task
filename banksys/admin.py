from django.contrib import admin
from .models import customers,transactionhistory

# Register your models here.
admin.site.register(customers)
admin.site.register(transactionhistory)
