from rest_framework import generics
from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class RetrieveNoteView(generics.RetrieveAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        return queryset

    def get_object(self):
        note_id = self.kwargs['pk']
        try:
            return self.get_queryset().get(id=note_id)
        except Note.DoesNotExist:
            return self.get_queryset().get(name=note_id)




# @api_view(['GET'])
# def get_note_view(request, pk):
#     note = get_object_or_404(Note, id=pk)
#     serializer = NoteSerializer(note)
#     return Response(serializer.data)



# @api_view(['GET', 'POST'])
# def note_list_create_view(request):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)