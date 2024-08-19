from django.urls import path
from .views import AddInvoiceItemView, InvoiceCreateView, InvoiceDetailView, InvoiceListView, SignInView, SignUpView

urlpatterns = [
    path('invoices/', InvoiceListView.as_view(), name='invoice-list'),
    path('invoices/new/', InvoiceCreateView.as_view(), name='invoice-create'),
    path("invoices/<uuid:id>/", InvoiceDetailView.as_view(), name="invoice-detail"),
    path('invoices/<uuid:invoice_id>/items/', AddInvoiceItemView.as_view(), name='add-invoice-item'),
    path('user/signup/', SignUpView.as_view(), name='user-signup'),
    path('user/login/', SignInView.as_view(), name='user-login'),
    # path('', InvoiceList.as_view(), name="allInvoices"),
    # path('newInvoice', InvoiceList.as_view(), name="addInvoice"),
    # path(':id/deleteInvoice', InvoiceItem.as_view(), name="deleteInvoice"),
    # path(':id/editInvoice', InvoiceItem.as_view(), name="editInvoice"),
    # path(':id', InvoiceItem.as_view(), name="readInvoiceItem"),
    # path(':id/newItem', InvoiceItem.as_view(), name="addInvoiceItem"),
    # path(':id/editItem', InvoiceItem.as_view(), name="editInvoiceItem"),
    # path(':id/deleteItem', InvoiceItem.as_view(), name="deleteInvoiceItem"),
]
