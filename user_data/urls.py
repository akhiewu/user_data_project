from django.urls import path
from .views import ParentListCreateView, ParentUpdateDeleteView, ChildListCreateView, ChildUpdateDeleteView

urlpatterns = [
    path('parents/', ParentListCreateView.as_view(), name='parent-list-create'),
    path('parents/<int:pk>/', ParentUpdateDeleteView.as_view(), name='parent-update-delete'),
    path('children/', ChildListCreateView.as_view(), name='child-list-create'),
    path('children/<int:pk>/', ChildUpdateDeleteView.as_view(), name='child-update-delete'),
]
