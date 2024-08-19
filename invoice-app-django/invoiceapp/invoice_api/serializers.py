from rest_framework import serializers
from .models import Invoice, InvoiceItem
from .models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import DatabaseError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        required=True
    )  # Ensure it's required if it should be
    name = serializers.CharField(required=False, allow_blank=True)  # Optional

    class Meta:
        model = User
        fields = ("username", "email", "name", "password")

    def validate_username(self, value):
        print(f"Validating username: {value}")
        try:
            # Attempt to get a user with the provided username
            user = User.objects.get(username=value)
            # If the user is found, raise a validation error
            print("Username exists, raising ValidationError")
            raise serializers.ValidationError("Username is already taken.")
        except User.DoesNotExist:
            # If no user is found, the username is available
            print("Username is available")
            return value

    def validate_email(self, value):
        print(f"Validating email: {value}")
        if not value:
            print("Email is empty, raising ValidationError")
            raise serializers.ValidationError("Email field cannot be empty.")
        print("Email is valid")
        return value

    def create(self, validated_data):
        print(f"Creating user with data: {validated_data}")
        try:
            user = User.objects.create_user(
                username=validated_data["username"],
                password=validated_data["password"],
                email=validated_data["email"],
                name=validated_data.get("name"),
            )
            print(f"User created successfully: {user}")
            return user
        except DjangoValidationError as e:
            print(f"Validation error occurred: {e}")
            raise serializers.ValidationError({"username": str(e)})
        except DatabaseError as e:
            print(f"Database error occurred: {e}")
            raise serializers.ValidationError({"database_error": str(e)})


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ["id", "description", "rate", "quantity", "createdAt", "updatedAt"]


class InvoiceSerializer(serializers.ModelSerializer):
    # items = InvoiceItemSerializer(many=True, write_only=True)

    class Meta:
        model = Invoice
        fields = [
            "id",
            "title",
            "status",
            "totalAmount",
            "clientName",
            "createdAt",
            "updatedAt",
        ]
        read_only_fields = ["id", "createdAt", "updatedAt"]

    def create(self, validated_data):
        # items_data = validated_data.pop("items")
        invoice = Invoice.objects.create(**validated_data)
        # for item_data in items_data:
            # InvoiceItem.objects.create(invoice=invoice, **item_data)
        return invoice


class InvoiceDetailSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            "id",
            "title",
            "status",
            "totalAmount",
            "clientName",
            "items",
            "createdAt",
            "updatedAt",
        ]
        read_only_fields = ["id", "createdAt", "updatedAt"]


class InvoiceItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ["id", "description", "rate", "quantity", "createdAt", "updatedAt"]
        read_only_fields = ["id", "createdAt", "updatedAt"]
