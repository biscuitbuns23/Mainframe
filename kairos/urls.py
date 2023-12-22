from django.urls import path
from .views import (KairosLanding, CreateAccount, WMFormsView,
                    CardsView, ChartsView)

app_name = "kairos"

urlpatterns = [
    path('', KairosLanding.as_view(), name='kairos-landing'),
    path('createaccount/', CreateAccount.as_view(), name='createaccount'),
    path('forms/', WMFormsView.as_view(), name='forms'),
    path('cards/', CardsView.as_view(), name='cards'),
    path('charts/', ChartsView.as_view(), name='charts'),
]