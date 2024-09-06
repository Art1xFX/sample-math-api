import math
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema
from .serializers import LogarithmSerializer, SquareRootSerializer, PowerSerializer, FactorialSerializer


@extend_schema(
    tags=['Calculator'],
)
class LogarithmView(APIView):
    @extend_schema(
        request=LogarithmSerializer,
        responses={200: LogarithmSerializer}
    )
    def post(self, request):
        serializer = LogarithmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Calculator'],
)
class SquareRootView(APIView):
    @extend_schema(
        request=SquareRootSerializer,
        responses={200: SquareRootSerializer}
    )
    def post(self, request):
        serializer = SquareRootSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Calculator'],
)
class PowerView(APIView):
    @extend_schema(
        request=PowerSerializer,
        responses={200: PowerSerializer}
    )
    def post(self, request):
        serializer = PowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Calculator'],
)
class FactorialView(APIView):
    @extend_schema(
        request=FactorialSerializer,
        responses={200: FactorialSerializer}
    )
    def post(self, request):
        serializer = FactorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
