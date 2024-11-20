from django.urls import path
from .views import TareaViewSet
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()

router.register(r'tareas', TareaViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API de Tareas",
      default_version='v1',
      description="API para la gestión de tareas.",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   
)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]

