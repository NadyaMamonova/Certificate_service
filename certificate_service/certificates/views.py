from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Certificate
from .serializers import CertificateSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def certificate_detail(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    serializer = CertificateSerializer(certificate)
    return Response(serializer.data)


@api_view(['GET'])
def certificates_by_email(request):
    email = request.query_params.get('email')
    if not email:
        return Response(
            {'error': 'Email parameter is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    certificates = Certificate.objects.filter(user__email=email)
    serializer = CertificateSerializer(certificates, many=True)
    return Response({'certificates': serializer.data})


@api_view(['GET'])
def certificates_without_skills(request):
    certificates = Certificate.objects.filter(skills__isnull=True)
    serializer = CertificateSerializer(certificates, many=True)
    return Response({'certificates': serializer.data})
