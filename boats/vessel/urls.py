from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('vessels', views.VesselViewSet, basename='Vessel')

urlpatterns = [
    path('', include(router.urls)),
    path('vessels/<code>/movements/',
         views.MovementHistoryViewSet.as_view({'get': 'list'})),
]
