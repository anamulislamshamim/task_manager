from django import forms 

from .models import Task


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = (
            "priority",
            "title",
            "description",
            "image",
            "is_complete"
        )
    
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            
        }


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = (
            "priority",
            "title",
            "description",
            "image",
        )
    
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            
        }