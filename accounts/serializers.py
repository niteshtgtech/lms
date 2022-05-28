# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import libraryModel

# Create a model serializer
class librarySerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = libraryModel
		fields = '__all__'
