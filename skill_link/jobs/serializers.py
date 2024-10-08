from rest_framework import serializers
from .models import JobPosting


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id', 'employer', 'title', 'description', 'required_skills']
        read_only_fields = ['employer']
