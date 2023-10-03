from django.contrib import admin
from django.urls import path
from .views import(
    PassDownCreateView, EntryCreateView, EntryListView, EntryByPassdown,
    DashboardView, PassDownListView, PassDownDetailView, MasterListView,
    MasterListView2, SearchView, SearchResultsView, SearchTestView
    )

app_name = "passdown"

urlpatterns = [
    path('', PassDownCreateView.as_view(), name='passdown-create'),
    path('createentry', EntryCreateView.as_view(), name='entry-create'),
    path('entrylist', EntryListView.as_view(), name='entry-list'),
    path('entrybypassdown', EntryByPassdown.as_view(), name='entry-by-passdown'),
    path('passdowndashboard', DashboardView.as_view(), name='dashboard'),
    path('masterlistboard', MasterListView2.as_view(), name='master-list'),
    path('passdownlist', PassDownListView.as_view(), name='passdownlist'),
    path('<int:pk>/', PassDownDetailView.as_view(), name='passdowndetail'),
    path('passdownsearchresults', SearchResultsView.as_view(), name='search-results'),
    path('passdownsearch', SearchView.as_view(), name='search'),
    path('passdownsearchtest', SearchTestView.as_view(), name='search-test'),




]