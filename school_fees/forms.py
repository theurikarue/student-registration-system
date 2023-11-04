from django import forms
from .models import Finance

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['student', 'Total_fee', 'Fee_paid', 'Fee_balance']
