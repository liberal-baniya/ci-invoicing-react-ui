import uuid
from django.db import models





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
