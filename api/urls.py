from django.urls import path
from .views import DumpItAPI

urlpatterns = [
    path('', DumpItAPI.as_view()),
    path('create', DumpItAPI.as_view()),
    path('update/<int:id>', DumpItAPI.as_view()),
    path('delete/<int:id>', DumpItAPI.as_view()),
]