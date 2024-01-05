from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.create_person,name='add_person'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
    path('connect/',views.connect,name='connect'),
    path('success/',views.success,name='success'),
]
