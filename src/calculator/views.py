from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiExample
from .serializers import LogarithmSerializer, SquareRootSerializer, PowerSerializer, FactorialSerializer


@extend_schema(
    tags=['Calculator'],
)
class LogarithmView(APIView):
    @extend_schema(
        summary="Compute Logarithm",
        description=(
            "This endpoint computes the logarithm of a given value with a specified base. "
            "Both the `base` and `value` must be greater than 0. The result will be returned "
            "as a floating-point number."
        ),
        request=LogarithmSerializer,
        responses={
            200: LogarithmSerializer
        },
        examples=[
            OpenApiExample(
                "Logarithm example",
                value={
                    "base": 2,
                    "value": 8
                },
                request_only=True,
                description="This example demonstrates how to compute the logarithm of 8 with base 2.",
            ),
            OpenApiExample(
                "Logarithm response",
                value={
                    "result": 3.0
                },
                response_only=True,
                description="The response for the logarithm of 8 with base 2.",
            ),
        ]
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
        summary="Compute Square Root",
        description=(
            "This endpoint computes the square root of a given number. "
            "It supports both real and complex numbers. If the input is a negative "
            "number, the result will be a complex number represented as a string "
            "with 'i' instead of Python's default 'j'. If the result is a real number, "
            "it will be returned as a floating-point number."
        ),
        request=SquareRootSerializer,
        responses={
            200: SquareRootSerializer
        },
        examples=[
            OpenApiExample(
                "Real number example",
                value={
                    "value": 16
                },
                request_only=True,
                description="This example demonstrates how to compute the square root of a positive real number.",
            ),
            OpenApiExample(
                "Complex number example",
                value={
                    "value": -16
                },
                request_only=True,
                description="This example demonstrates how to compute the square root of a negative number, returning a complex result.",
            ),
            OpenApiExample(
                "Real number response",
                value={
                    "result": 4.0
                },
                response_only=True,
                description="The response for a real number (e.g., square root of 16).",
            ),
            OpenApiExample(
                "Complex number response",
                value={
                    "result": "4i"
                },
                response_only=True,
                description="The response for a complex number (e.g., square root of -16).",
            ),
        ]
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
        summary="Compute Power",
        description=(
            "This endpoint computes the power of a given base raised to a specified exponent. "
            "Both `base` and `exp` can be any real numbers. The result is returned as a floating-point number."
        ),
        request=PowerSerializer,
        responses={
            200: PowerSerializer,
        },
        examples=[
            OpenApiExample(
                "Power example",
                value={
                    "base": 2,
                    "exp": 3
                },
                request_only=True,
                description="This example demonstrates how to compute 2 raised to the power of 3.",
            ),
            OpenApiExample(
                "Power response",
                value={
                    "result": 8.0
                },
                response_only=True,
                description="The response for 2 raised to the power of 3.",
            ),
        ]
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
        summary="Compute Factorial",
        description=(
            "This endpoint computes the factorial of a given integer value. "
            "`value` must be a non-negative integer. The result is returned as an integer."
        ),
        request=FactorialSerializer,
        responses={
            200: FactorialSerializer,
        },
        examples=[
            OpenApiExample(
                "Factorial example",
                value={
                    "value": 5
                },
                request_only=True,
                description="This example demonstrates how to compute the factorial of 5.",
            ),
            OpenApiExample(
                "Factorial response",
                value={
                    "result": 120
                },
                response_only=True,
                description="The response for the factorial of 5.",
            ),
        ]
    )
    def post(self, request):
        serializer = FactorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
