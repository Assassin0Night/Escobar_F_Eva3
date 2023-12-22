from rest_framework import serializers
from App_Escobar_F import models

class inscripcionSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Inscrito
        fields = '__all__'
        
class institucionSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Institucion
        fields = '__all__'