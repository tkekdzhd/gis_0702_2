from django.forms import ModelForm
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        # 클라이언트로부터 입력받는 fields
        fields = ['name', 'image', 'description']
