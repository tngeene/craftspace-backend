from django.urls import include, path

from products.apiv1.views.products import (CategoryAPIView,
                                           CategoryDetailAPIView,
                                           ProductCreateAPIView,
                                           ProductDestroyAPIView,
                                           ProductDetailsAPIView,
                                           ProductListAPIView,
                                           ProductUpdateAPIView)

urlpatterns = [
    path('all-art-pieces/',ProductListAPIView.as_view(),name='all_pieces'),
    path('add/', ProductCreateAPIView.as_view(),name='product_add'),
    path('<int:pk>/edit/', ProductUpdateAPIView.as_view(),name='product_edit'),
    path('<int:pk>/', ProductDetailsAPIView.as_view(),name='product_details'),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view(),name='product_destroy'),

    # category routes
    path('art-categories/', CategoryAPIView.as_view(),name='art_categories'),
    path('art-categories/<int:pk>', CategoryDetailAPIView.as_view(),name='art_categories_rud'),
]
