from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name!"}
        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Your Feedback!"}
        )
    )