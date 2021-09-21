from savers.models import Saver
from rest_framework import viewsets, permissions
from .serializers import SaverSerializer

class SaverViewSet(viewsets.ModelViewSet):
    queryset = Saver.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class=SaverSerializer