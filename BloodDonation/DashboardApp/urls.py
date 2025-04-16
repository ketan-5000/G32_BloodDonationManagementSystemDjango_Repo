from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('donate/', views.add_donation_view, name='add_donation'), 
    path('request/', views.request_blood_view, name='request_blood'), 
    path('donation/edit/<int:donation_id>/', views.edit_donation_view, name='edit_donation'),
    path('donation/delete/<int:donation_id>/', views.delete_donation_view, name='delete_donation'),
]
