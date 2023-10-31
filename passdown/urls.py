from django.urls import path
from .views import(
    PassDownCreateView, EntryCreateView,
    MasterListView2, SearchView, SearchResultsView, AdminDashboardView,
    SearchResultsEntryView, NoPermissionView
    )

app_name = "passdown"

urlpatterns = [
    path('', PassDownCreateView.as_view(), name='passdown-create'),
    path('createentry', EntryCreateView.as_view(), name='entry-create'),

    path('masterlistboard', MasterListView2.as_view(), name='master-list'),

    path('passdownsearchresults', SearchResultsView.as_view(), name='search-results'), # Search returns entire passdown
    path('passdownsearchresultsbyentry', SearchResultsEntryView.as_view(), name='search-results-entries'), # Search returns entries only
    path('passdownsearch', SearchView.as_view(), name='search'),

    path('admindashboard', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('notauthorized', NoPermissionView.as_view(), name='not-authorized'),
]