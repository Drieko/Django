# serializers.py
from rest_framework import serializers
from datetime import datetime

class FilmeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=100)
    diretor = serializers.CharField(max_length=100)
    ano = serializers.IntegerField()
    genero = serializers.CharField(max_length=100)
    sinopse = serializers.CharField()

    class Meta:
        fields = ('id', 'titulo', 'diretor', 'ano', 'genero', 'sinopse')

    def validate_ano(self, value):
        if value < 1900 or value > datetime.now().year:
            raise serializers.ValidationError("O ano do filme deve estar entre 1900 e o ano atual.")
        return value