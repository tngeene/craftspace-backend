from core.models import Event
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from products.models import Product

from .dashboard import DashboardView

User = get_user_model()

# view for confirming user suspension
class UserConfirmSuspendView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'

# logic for suspending users and redirection based on user type
def suspend_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()

    if(user.membership_type == 'Artist'):
        messages.success(request,"Account Suspended")
        return redirect("dashboard:artist_details", pk=pk)
    elif(user.membership_type == 'Staff'):
        messages.success(request,"Account Suspended")
        return redirect("dashboard:staff_details", pk=pk)
    elif(user.membership_type == 'Collector'):
        messages.success(request,"Account Suspended")
        return redirect("dashboard:collector_details", pk=pk)

# logic for activating users and redirection
def activate_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = True
    user.save()

    if(user.membership_type == 'Artist'):
        messages.success(request,"Account activated")
        return redirect("dashboard:artist_details", pk=pk)
    elif(user.membership_type == 'Staff'):
        messages.success(request,"Account activated")
        return redirect("dashboard:staff_details", pk=pk)
    elif(user.membership_type == 'Collector'):
        messages.success(request,"Account activated")
        return redirect("dashboard:collector_details", pk=pk)

# event approve or reject
def approve_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.is_approved = True
    event.save()

    messages.success(request, "Event Approved")
    return redirect("dashboard:event_details", pk=pk)

def reject_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.is_approved = not event.is_approved
    event.save()

    messages.success(request, "Event Rejected")
    return redirect("dashboard:event_details", pk=pk)


# view to prompt user if they want to reject a product
class ProductConfirmRejectView(DashboardView, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'dashboard/products/confirm-reject.html'

# product approve or reject
def approve_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_approved = True
    product.save()

    messages.success(request, "Product Approved")
    return redirect("dashboard:product_details", pk=pk)

def reject_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_approved = not product.is_approved
    product.save()

    messages.success(request, "Product Rejected")
    return redirect("dashboard:product_details", pk=pk)


