from django import forms
from django.forms.widgets import CheckboxSelectMultiple, DateTimeInput

from todo.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "tags", "deadline"]
