from rest_framework import serializers
from .models import Certificate, Links

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ('link_name', 'link')
        
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('name', 'last_name', 'course_name', 'email', 'phone_number', 'links')
    links = LinksSerializer(many=True)
