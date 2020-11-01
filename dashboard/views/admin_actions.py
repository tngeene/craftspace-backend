from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .dashboard import DashboardView
from django.contrib.auth import get_user_model

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



