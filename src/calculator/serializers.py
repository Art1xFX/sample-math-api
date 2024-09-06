from rest_framework import serializers
import math

class LogarithmSerializer(serializers.Serializer):
    base = serializers.FloatField(min_value=0.0001, write_only=True, required=True)
    value = serializers.FloatField(min_value=0.0001, write_only=True, required=True)
    result = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        base = validated_data['base']
        value = validated_data['value']
        validated_data['result'] = math.log(value, base)
        return validated_data


class SquareRootSerializer(serializers.Serializer):
    value = serializers.FloatField(min_value=0, write_only=True, required=True)
    result = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        value = validated_data['value']
        validated_data['result'] = math.sqrt(value)
        return validated_data


class PowerSerializer(serializers.Serializer):
    base = serializers.FloatField(write_only=True, required=True)
    exp = serializers.FloatField(write_only=True, required=True)
    result = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        base = validated_data['base']
        exp = validated_data['exp']
        validated_data['result'] = math.pow(base, exp)
        return validated_data


class FactorialSerializer(serializers.Serializer):
    value = serializers.IntegerField(min_value=0, write_only=True, required=True)
    result = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        value = validated_data['value']
        validated_data['result'] = math.factorial(value)
        return validated_data
