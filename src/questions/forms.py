from django import forms


class QuestionListForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('-created', 'newest'),
        ('title', 'title')
    ), required=False)
    search = forms.CharField(required=False)


class AnswerForm(forms.Form):
    text = forms.CharField(required=True)

