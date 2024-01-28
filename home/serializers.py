from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# ModelSerializer
from .models import name

class nameserializer(serializers.ModelSerializer):
    # id = serializers.CharField()
    username = serializers.CharField(max_length= 100)
    bio = serializers.CharField(max_length= 200)
    class Meta:
        model = name
        fields = '__all__' 
    # def validate(self , data):
    #     nm = data.get('username')
    #     bio = data.get('bio') 
    #     if nm == 'bassi':
    #         raise serializer.ValidationError('no name as bassi')
    #     return data
    # def update(self , instance , validated_data):
    #     instance.username = validated_data['username' , instance.username]
    #     instance.bio = validated_data['bio' , instance.bio]
    #     instance.save()
    #     return instance  
             