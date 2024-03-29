from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from . models import Person, Branch

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        
        widgets = {
        'DOB': forms.DateInput(attrs={'type': 'date'}),
        'gender': forms.RadioSelect(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]),
    }
        
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()
        common_attrs = {
            'class': 'form-control',
            'style': 'max-width: 300px;',
        }

        for field_name, field in self.fields.items():
 
            if isinstance(field.widget, (TextInput, EmailInput)):
                field.widget.attrs.update(common_attrs)
            
            elif isinstance(field.widget, forms.Select):
                select_attrs = {
                    'class': 'form-control',
                    'style': 'max-width: 300px;',
                }
                select_attrs.update(common_attrs)
                field.widget.attrs.update(select_attrs)

            
            
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
                
            elif field_name in ['age', 'address']:
                field.widget.attrs.update(common_attrs)
                
        self.fields['gender'].empty_label = None
        
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')