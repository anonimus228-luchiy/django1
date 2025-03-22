from django import forms
from django.template.defaulttags import querystring

from posts.models import Post, Category


# class PostCreateForm(forms.Form):
#     image = forms.ImageField()
#     title = forms.CharField()
#     content = forms.CharField()
#
#     def clean_title(self):
#         cleaned_data = super().clean()
#         title = cleaned_data.get("title")
#         if title and title.lower() == "con":
#             raise forms.ValidationError("This is not a valid title")
#         return title
#
#     def clean(self):
#         cleaned_data = super().clean()
#         content = cleaned_data.get("content")
#         title = cleaned_data.get("title")
#         if title and content and title.lower() in content.lower():
#             raise forms.ValidationError("Title should not be in content")
#         return cleaned_data

class PostCreateForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image"]


def clean_title(self):
    cleaned_data = super().clean()
    title = cleaned_data.get("title")
    if title and title.lower() == "con":
        raise forms.ValidationError("This is not a valid title")
    return title


def clean(self):
    cleaned_data = super().clean()
    content = cleaned_data.get("content")
    title = cleaned_data.get("title")
    if title and content and title.lower() in content.lower():
        raise forms.ValidationError("Title should not be in content")
    return cleaned_data

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100,required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),required=False,widget=forms.Select
    )
    orderings =(
        ("created_at","По дате создания "),
        ("-created_at","По дате создания в обратном порядке"),
        ("title","По названию"),
        ("-title","По названию в обратном порядке"),
        ("rate" ,"По рейтингу"),
        ("-rate","По рейтингу в обратном порядке"),
        (None ,"Без сортировки")

    )
    ordering = forms.ChoiceField(choices=orderings,required=False)