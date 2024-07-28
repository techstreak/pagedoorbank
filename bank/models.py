# bank/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone




class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='bank_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='bank_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s account with balance {self.balance}"

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10)  # 'credit' or 'debit'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    receiver_id = models.IntegerField(null=True, blank=True)  # New field to store receiver ID if applicable
    description = models.CharField(max_length=255, blank=True)  # New field to store a description of the transaction

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp}"
