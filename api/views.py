from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import Note

# Create your views here.

"""
API Overview
"""


@api_view(['GET'])
def api_overview(request):
    urls = {
        'List': '/note-list/',
        'Detail View': '/note-detail/<str:pk>/',
        'Create': '/note-create/',
        'Update': '/note-update/<str:pk>/',
        'Delete': '/note-delete/<str:pk>/'
    }
    return Response(urls)

"""
Below Function going to display all the notes stored in the data base.
"""
@api_view(['GET'])
def note_list(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)