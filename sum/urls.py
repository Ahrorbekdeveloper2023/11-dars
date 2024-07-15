from django.urls import path, include

from rest_framework import routers
from .views import DailyCostModelViewSet

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.SimpleRouter()
router.register('like', DailyCostModelViewSet)



urlpatterns = [
    path('api/v1/', include(router.urls)),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api-auth/', include('rest_framework.urls'))
]