from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from . import models, serializers, permissions


class VesselViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.VesselSerializer
    permission_classes = [IsAuthenticated, permissions.IsOwner]
    lookup_field = 'code'

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Vessel.objects.all()
        return models.Vessel.objects.filter(owner=self.request.user)


class MovementHistoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.MovementHistorySerializer
    permission_classes = [IsAuthenticated, permissions.IsOwner]

    def get_object(self):
        obj = get_object_or_404(
            models.Vessel.objects.filter(code=self.kwargs['code'])
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        self.get_object()
        return models.MovementHistory.objects \
            .filter(vessel__code=self.kwargs['code'])
