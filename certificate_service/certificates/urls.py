from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:certificate_id>/', views.certificate_detail, name='certificate-detail'),
    path('by-email/', views.certificates_by_email, name='certificates-by-email'),
    path('without-skills/', views.certificates_without_skills, name='certificates-without-skills'),
]