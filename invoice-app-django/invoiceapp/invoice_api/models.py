import uuid
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError as DjangoValidationError


# from djongo import models
import uuid
import logging
from django.db.utils import DatabaseError

class UserManager(BaseUserManager):
    def create_user(self, username, password, email, name=None, **extra_fields):
        if not username:
            raise ValueError("Username should be provided")
        if not email:
            raise ValueError("Email should be provided")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, name=name, **extra_fields)
        user.set_password(password)

        try:
            user.save(using=self._db)
        except DatabaseError as e:
            if "duplicate key" in str(e):
                raise DjangoValidationError(f"Username '{username}' is already taken.")
            else:
                raise DjangoValidationError(f"An error occurred: {str(e)}")

        print(
            f"Created user: {user.username}, is_staff: {user.is_staff}, is_superuser: {user.is_superuser}"
        )
        return user

    def create_superuser(self, username, password, email, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.create_user(username, password, email, **extra_fields)
        print(
            f"Created superuser: {user.username}, is_staff: {user.is_staff}, is_superuser: {user.is_superuser}"
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=100, unique=True)
    refresh_token = models.CharField(max_length=300, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.username




class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    totalAmount = models.DecimalField(decimal_places=2, max_digits=12)  # Adjust max_digits as needed
    clientName = models.CharField(max_length=255)

    class Meta:
        ordering = ['-updatedAt']

    def __str__(self) -> str:
        return self.title

class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    description = models.TextField()
    rate = models.DecimalField(decimal_places=2, max_digits=10)  # Adjust max_digits as needed
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updatedAt']

    def __str__(self) -> str:
        return self.description
