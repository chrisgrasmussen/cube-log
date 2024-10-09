from rest_framework import generics
from .models import Solve
from .serializers import SolveSerializer

from rest_framework import status
from rest_framework.response import Response

class SolveListCreateView(generics.ListCreateAPIView):
    queryset = Solve.objects.all()
    serializer_class = SolveSerializer
    
    
class SolveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solve.objects.all()
    serializer_class = SolveSerializer
    
class AllSolvesListView(generics.ListAPIView):
    queryset = Solve.objects.all()
    serializer_class = SolveSerializer
    
class SolveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Solve.objects.all()
    serializer_class = SolveSerializer
    partial = True
    
    
class SolveDeleteView(generics.DestroyAPIView):
    queryset = Solve.objects.all()
    serializer_class = SolveSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Solve"))