from django.urls import path
from . import views
app_name = 'day3app'
urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='all'),
    path('<int:pk>/detail', views.EmployeeDetailView.as_view(),
         name='employee_detail'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/update/', views.EmployeeUpdateView.as_view(),
         name='employee_update'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(),
         name='employee_delete'),
]
