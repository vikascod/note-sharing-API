from django.urls import path
from notes import views

urlpatterns = [
    path('notes/', views.NoteListCreateView.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.RetrieveNoteView.as_view(), name='note-retrieve'),

]


