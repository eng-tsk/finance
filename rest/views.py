from rest_framework import generics
from rest.models import History
from rest.serializers import HistorySerializer
 
class HistoryListACreateAPIView(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer