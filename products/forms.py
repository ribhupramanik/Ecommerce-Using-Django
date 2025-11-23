from django import forms
from .models import ProductReview, Product

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'review_text']

        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5
            }),
            'review_text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your review...'
            })
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']