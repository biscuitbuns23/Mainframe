from django.contrib import admin
from django.urls import path
from .views import(
    PassDownCreateView, EntryCreateView, EntryListView, EntryByPassdown,
    DashboardView, PassDownListView, PassDownDetailView, MasterListView,
    MasterListView2
    )

app_name = "passdown"

urlpatterns = [
    path('', PassDownCreateView.as_view(), name='passdown-create'),
    path('createentry', EntryCreateView.as_view(), name='entry-create'),
    path('entrylist', EntryListView.as_view(), name='entry-list'),
    path('entrybypassdown', EntryByPassdown.as_view(), name='entry-by-passdown'),
    path('passdowndashboard', DashboardView.as_view(), name='dashboard'),
    path('masterlistboard', MasterListView.as_view(), name='master-list'),
    path('masterlistboard2', MasterListView2.as_view(), name='master-list2'),
    path('passdownlist', PassDownListView.as_view(), name='passdownlist'),
    path('<int:pk>/', PassDownDetailView.as_view(), name='passdowndetail'),

]