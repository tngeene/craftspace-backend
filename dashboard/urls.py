from django.urls import path

from dashboard.views.dashboard import DashboardTemplateView

from .views.admin_actions import (ProductConfirmRejectView,
                                  UserConfirmSuspendView, activate_user,
                                  approve_event, approve_product, reject_event,
                                  reject_product, suspend_user)
from .views.artists import ArtistDetailView, ArtistListView, ArtistUpdateView
from .views.collectors import (CollectorDetailView, CollectorListView,
                               CollectorUpdateView)
from .views.events import (EventCreateView, EventDetailView, EventListView,
                           EventUpdateView)
from .views.orders import (CustomOrderDetailView, CustomOrderListView,
                           OrderDetailView, OrderListView)
from .views.products import (CategoryCreateView, CategoryDetailView,
                             CategoryListView, CategoryUpdateView,
                             ProductDetailView, ProductListView)

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='index'),

    # admin action urls
    path('users/<int:pk>/confirm-suspend/',
         UserConfirmSuspendView.as_view(), name="user_confirm_suspend"),
    path('users/<int:pk>/suspend_user/',
         suspend_user, name="user_suspend_action"),
    path('users/<int:pk>/unsuspend_user/',
         activate_user, name="user_unsuspend_action"),
    path('events/<int:pk>/reject/', reject_event, name="event_reject_action"),
    path('events/<int:pk>/approve/', approve_event, name="event_approve_action"),
    path('products/<int:pk>/confirm-reject/',
         ProductConfirmRejectView.as_view(), name="product_confirm_reject"),
    path('products/<int:pk>/reject/', reject_product,
         name="product_reject_action"),
    path('products/<int:pk>/approve/', approve_product,
         name="product_approve_action"),

    # artist urls
    path('artists/all/', ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/details/',
         ArtistDetailView.as_view(), name='artist_details'),
    path('artists/<int:pk>/edit/', ArtistUpdateView.as_view(), name='artist_edit'),

    # collector urls
    path('collectors/all/', CollectorListView.as_view(), name='collector_list'),
    path('collectors/<int:pk>/details/',
         CollectorDetailView.as_view(), name='collector_details'),
    path('collectors/<int:pk>/edit/',
         CollectorUpdateView.as_view(), name='collector_edit'),

    # event urls
    path('events/all/', EventListView.as_view(), name="event_list"),
    path('events/add/', EventCreateView.as_view(), name="event_create"),
    path('events/<int:pk>/details/',
         EventDetailView.as_view(), name="event_details"),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name="event_edit"),

    # product urls
    path('products/categories/all/', CategoryListView.as_view(),
         name='product_category_list'),
    path('products/categories/add/', CategoryCreateView.as_view(),
         name='product_category_add'),
    path('products/categories/<int:pk>/details/',
         CategoryDetailView.as_view(), name='product_category_details'),
    path('products/categories/<int:pk>/edit/',
         CategoryUpdateView.as_view(), name="product_category_edit"),
    path('products/all/', ProductListView.as_view(), name="product_list"),
    path('products/<int:pk>/details',
         ProductDetailView.as_view(), name="product_details"),

    # order urls
    path('orders/all/', OrderListView.as_view(), name="order_list"),
    path('orders/<int:pk>/details/',
         OrderDetailView.as_view(), name="order_details"),
    path('custom-orders/all/', CustomOrderListView.as_view(),
         name="custom_order_list"),
    path('custom-orders/<int:pk>/details/',
         CustomOrderDetailView.as_view(), name="custom_order_details"),

]
