from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('note-list/', views.note_list, name="note-list"),
]
