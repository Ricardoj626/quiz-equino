from django import forms


from .models import Questionario

class nomeForm(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('nome', 'numero',)


class p1Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_1', )

class p2Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_2',)


class p3Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_3',)


class p4Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_4',)


class p5Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_5',)


class p6Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_6',)


class p7Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_7',)


class p8Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_8',)


class p9Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_9',)


class p10Form(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ('pergunta_10',)

