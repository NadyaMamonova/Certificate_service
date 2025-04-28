from rest_framework import serializers
from .models import Certificate, User, Internship, Role, Skill


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'category']


class CertificateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    skills = SkillSerializer(many=True)

    class Meta:
        model = Certificate
        fields = '__all__'