from django import forms


class CategoryListForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('name', 'name'),
        ('-name', '-name'),
    ), required=False)
    search = forms.CharField(required=False)


class CategoryForm(forms.Form):
    name = forms.CharField(required=True)