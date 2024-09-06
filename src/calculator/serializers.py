from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
import math
import cmath


class LogarithmSerializer(serializers.Serializer):
    base = serializers.FloatField(
        min_value=0.0001,
        write_only=True,
        required=True,
        help_text="Base of the logarithm, must be a positive number greater than 0."
    )
    value = serializers.FloatField(
        min_value=0.0001,
        write_only=True,
        required=True,
        help_text="Value for which the logarithm will be calculated, must be a positive number greater than 0."
    )
    result = serializers.FloatField(
        read_only=True,
        help_text="Result of the logarithm operation."
    )


    def create(self, validated_data):
        base = validated_data['base']
        value = validated_data['value']
        validated_data['result'] = math.log(value, base)
        return validated_data


class SquareRootSerializer(serializers.Serializer):
    value = serializers.FloatField(
        write_only=True,
        required=True,
        help_text="Number for which the square root will be calculated. It can be a negative number for complex results."
    )
    result = serializers.SerializerMethodField(
        help_text="Result of the square root operation. Can be real (number) or complex (string)."
    )

    @extend_schema_field(serializers.CharField())
    def get_result(self, obj):
        value = obj['value']
        result = cmath.sqrt(value)
        if result.imag == 0:
            return result.real
        return str(result).replace('j', 'i')

    def create(self, validated_data):
        return validated_data


class PowerSerializer(serializers.Serializer):
    base = serializers.FloatField(
        write_only=True,
        required=True,
        help_text="Base number to be raised to the power."
    )
    exp = serializers.FloatField(
        write_only=True,
        required=True,
        help_text="Exponent to which the base will be raised."
    )
    result = serializers.FloatField(
        read_only=True,
        help_text="Result of the power operation."
    )

    def create(self, validated_data):
        base = validated_data['base']
        exp = validated_data['exp']
        validated_data['result'] = math.pow(base, exp)
        return validated_data


class FactorialSerializer(serializers.Serializer):
    value = serializers.IntegerField(
        min_value=0,
        write_only=True,
        required=True,
        help_text="Non-negative integer value for which the factorial will be calculated.",
    )
    result = serializers.IntegerField(
        read_only=True,
        help_text="Result of the factorial operation.",
    )

    def create(self, validated_data):
        value = validated_data['value']
        validated_data['result'] = math.factorial(value)
        return validated_data
