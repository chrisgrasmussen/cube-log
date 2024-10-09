from django.urls import path
from .views import SolveListCreateView, SolveDetailView,AllSolvesListView,SolveDeleteView,SolveUpdateView

urlpatterns = [
    path('solves/', SolveListCreateView.as_view(), name='Solve-list-create'),
    path('solves/<int:pk>/', SolveDetailView.as_view(), name='Solve-detail'),
    path('solves/all/', AllSolvesListView.as_view(), name='all-Solves-list'),  
    path('solves/delete/<int:pk>/', SolveDeleteView.as_view(), name='Solve-delete'), 
    path('solves/update/<int:pk>/', SolveUpdateView.as_view(), name='Solve-update'), 
]