from rest_framework import viewsets, status
from .serializers import TareaSerializer
from .models import Tarea
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'estatus',  
                openapi.IN_QUERY,  
                description="Filtra las tareas por estado (pendiente, en progreso, completado).",
                type=openapi.TYPE_STRING, 
                enum=['pendiente', 'en progreso', 'completado'] 
            )
        ],
        operation_description="Filtra las tareas por estado."
    )
    @action(detail=False, methods=['get'], url_path='por-estado')
    def por_estado(self, request):
        """
        Filtra las tareas por estado.
        """
        estado = request.query_params.get('estatus')  
        if not estado:
            return Response(
                {"error": "El parámetro 'estatus' es obligatorio."},
                status=status.HTTP_400_BAD_REQUEST
            )

        tareas = self.queryset.filter(estatus=estado)
        serializer = self.get_serializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)