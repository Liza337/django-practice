from django.urls import path, include
from . import views
urlpatterns = [ 
path('', views.employee_list),
path('<int:pk>/', views.employee_detail), 
]
