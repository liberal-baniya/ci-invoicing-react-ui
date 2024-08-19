from rest_framework import generics
from .models import Invoice
from .serializers import (
    InvoiceItemAddSerializer,
    InvoiceSerializer,
    InvoiceDetailSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from .models import User
from django.http import Http404, JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # Generate refresh and access tokens
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            # Save the refresh token in the user model
            user.refresh_token = str(refresh)
            user.save()

            # Set cookies
            response = JsonResponse(
                {
                    "username": user.username,
                    "email": user.email,
                    "name": user.name,
                    "id": user.id,
                    "is_superuser": user.is_superuser,
                    "is_staff": user.is_staff,
                    "message": "Signup successful. User authenticated.",
                },
                status=status.HTTP_201_CREATED,
            )

            # Set cookies in the response
            response.set_cookie(
                "accessToken",
                str(access),
                httponly=True,
                secure=False,  # Set secure=True in production
                samesite="Lax",  # Adjust based on your security needs
            )
            response.set_cookie(
                "refreshToken",
                str(refresh),
                httponly=True,
                secure=False,  # Set secure=True in production
                samesite="Lax",  # Adjust based on your security needs
            )

            return response

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data  # This is the User instance directly

            # Generate refresh and access tokens
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            # Save the refresh token to the user model
            user.refresh_token = str(refresh)
            user.save()

            # Prepare the response data
            response_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "name": user.name,
                "is_staff": user.is_staff,  # Include is_staff to indicate admin privileges
                "is_superuser": user.is_superuser,
                "refresh": str(refresh),  # Convert to string
                "access": str(access),  # Convert to string
            }

            # Create the response object
            response = JsonResponse(response_data, status=status.HTTP_200_OK)

            # Set cookies in the response
            response.set_cookie(
                "accessToken",
                str(access),
                httponly=True,
                secure=False,  # Set secure=True in production
                samesite="Lax",
                path="/",  # Adjust based on your security needs
            )
            response.set_cookie(
                "refreshToken",
                str(refresh),
                httponly=True,
                secure=False,  # Set secure=True in production
                samesite="Lax",
                path="/",  # Adjust based on your security needs
            )

            return response

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List Invoices
class InvoiceListView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceDetailSerializer


# Create Invoices
class InvoiceCreateView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


# Retrieve a Specific Invoice
class InvoiceDetailView(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceDetailSerializer
    lookup_field = "id"


class AddInvoiceItemView(generics.CreateAPIView):
    serializer_class = InvoiceItemAddSerializer

    def post(self, request, invoice_id, *args, **kwargs):
        try:
            invoice = Invoice.objects.get(id=invoice_id)
        except Invoice.DoesNotExist:
            return Response(
                {"error": "Invoice not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(invoice=invoice)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
