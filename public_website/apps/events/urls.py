from django.urls import path
from events import views

# Template tagging Django reference
app_name = 'events'

urlpatterns = [
    path('create-event/', views.EventCreationView.as_view(), name='event_creation'),
    path('list/', views.EventsList.as_view(), name='event_list'),
    path('list/<slug:slug>/', views.EventSpecifics.as_view(), name='event_specifics'),

    path('create-group/', views.GroupCreationView.as_view(), name='group_creation'),
    path('register-group/', views.GroupRegisterView.as_view(), name='group_register'),

   ]
