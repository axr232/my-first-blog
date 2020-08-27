from django import forms 
from .models import Post
from .models import CV

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','text')

class CVForm(forms.ModelForm):
    
    class Meta:
        model = CV
        fields = ('address','phone_number','profile','education','experience','extracurricular_achievements','skills_and_interests')