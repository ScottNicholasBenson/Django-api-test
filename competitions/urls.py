from django.urls import path
from . import views

urlpatterns = [
    path('upload-competitions/', views.uploadCompetitions, name="upload-competitions"),
    path('upload-bids/', views.uploadBids, name="upload-bids"),
    path('upload-sellers/', views.uploadSellers, name="upload-sellers"),
    path('upload-buyers/', views.uploadBuyers, name="upload-buyers"),
    path('view-competitions/', views.viewCompetitions, name="view-competitions"),
    # path('view/', views.viewLocations, name="view-locations"),
    # path('list/', views.listLocations, name="list-locations"),
    # path('radius/', views.viewLocationsInRadius, name="view-radius"),
]
