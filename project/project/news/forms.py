from django import forms
from .models import News
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = News

        fields = [
            'author',
            'title',
            'text',
        ]

        def clean(self):
            cleaned_data = super().clean()
            author = cleaned_data.get("author")
            title = cleaned_data.get("title")

            if author == title:
                raise ValidationError(
                    "Описание не должно быть идентичным названию."
                )

            return cleaned_data

        ''' вот так мы можем проверить, написано ли название товара с заглавной буквы: '''

        def clean_name(self):
            author = self.cleaned_data['author']
            if author[0].islower():
                raise ValidationError(
                    'Название должно начинаться с заглавной буквы.'
                )

            return author






