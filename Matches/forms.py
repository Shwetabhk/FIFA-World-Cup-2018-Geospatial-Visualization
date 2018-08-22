from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Enter comments about this match", "rows":"4", "class": "form-control "}))

    def clean_comment(self):
        comment = self.cleaned_data.get("comment")
        if len(comment) > 180:
            raise forms.ValidationError("Maximum length allowed is 180")
        return comment
