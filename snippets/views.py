from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def overview(self, request):
        snippets = self.get_queryset()
        total_count = snippets.count()
        serializer = self.get_serializer(snippets, many=True)
        return Response({
            'total_count': total_count,
            'snippets': serializer.data
        })

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def snippets(self, request, pk=None):
        tag = self.get_object()
        snippets = Snippet.objects.filter(tags=tag)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
