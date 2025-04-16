from django.urls import path
from . import views
from DashboardApp.urls import views as v

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.register_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', v.dashboard_view, name='dashboard'),
    path('donate/', v.add_donation_view, name='add_donation'), 
    path('request/', v.request_blood_view, name='request_blood'), 
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
]
