# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
from .models import Account, Transaction
from rest_framework.authtoken.models import Token

try:
    from .models import User as CustomUser
    user_model = CustomUser
except ImportError:
    user_model = User

class UserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

admin.site.register(user_model, UserAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username', 'balance')
    list_filter = ('user__username',)
    fields = ('user', 'balance')

admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'timestamp')
    search_fields = ('account__user__username', 'transaction_type', 'amount')
    list_filter = ('transaction_type', 'timestamp')

admin.site.register(Transaction, TransactionAdmin)

class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user')
    search_fields = ('user__username',)

admin.site.register(Token, TokenAdmin)
