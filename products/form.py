from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    # email = forms.EmailField()
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Your description",
                                          "class": "new_class_name two",
                                          "id": "my_id_for_textarea",
                                          "row": 20,
                                          "cols": 120
                                      }
                                  )
                                  )
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "Product" not in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title

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
