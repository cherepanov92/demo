# -*- coding: utf-8 -*-
from django import forms

class MyNameForm(forms.Form):
    name = forms.CharField(max_length=40)
