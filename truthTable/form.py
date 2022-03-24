from django import forms
from .models import Generator

from .truth_table_generator import generate


class TruthTableForm(forms.ModelForm):
    formula = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Formula"}))

    class Meta:
        model = Generator
        fields = [
            'formula'
        ]

    def clean_formula(self, *args, **kwargs):
        formula = self.cleaned_data.get("formula")

        try:
            generate(formula)
            return formula
        except IOError:
            raise forms.ValidationError("This formula is invalid")

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("title")
    #     if not email.endswith("com"):
    #         raise forms.ValidationError("This is not a valid email ")
    #     else:
    #         return email


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

