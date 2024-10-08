
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import JobPosting
from .serializers import JobPostingSerializer
from rest_framework.exceptions import PermissionDenied

class JobPostingListCreate(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

    def perform_create(self, serializer):
        if self.request.user.userprofile.role != 'employer':
            raise PermissionDenied("Only employers can create job postings.")
        serializer.save(employer=self.request.user)
