from django import forms

class CropRecommendationForm(forms.Form):
    nitrogen = forms.FloatField(
        label='Nitrogen (N)', min_value=10, max_value=120, 
        error_messages={'min_value': 'Nitrogen must be at least 10.', 'max_value': 'Nitrogen must be at most 120.'}
    )
    phosphorus = forms.FloatField(
        label='Phosphorus (P)', min_value=10, max_value=150, 
        error_messages={'min_value': 'Phosphorus must be at least 10.', 'max_value': 'Phosphorus must be at most 150.'}
    )
    potassium = forms.FloatField(
        label='Potassium (K)', min_value=10, max_value=200, 
        error_messages={'min_value': 'Potassium must be at least 10.', 'max_value': 'Potassium must be at most 200.'}
    )
    temperature = forms.FloatField(
        label='Temperature (°C)', min_value=5, max_value=35, 
        error_messages={'min_value': 'Temperature must be at least 5°C.', 'max_value': 'Temperature must be at most 35°C.'}
    )
    humidity = forms.FloatField(
        label='Humidity (%)', min_value=10, max_value=100, 
        error_messages={'min_value': 'Humidity must be at least 10%.', 'max_value': 'Humidity must be at most 100%.'}
    )
    ph = forms.FloatField(
        label='pH Level', min_value=1, max_value=15, 
        error_messages={'min_value': 'pH must be at least 1.', 'max_value': 'pH must be at most 15.'}
    )
    rainfall = forms.FloatField(
        label='Rainfall (mm)', min_value=10, max_value=300, 
        error_messages={'min_value': 'Rainfall must be at least 10mm.', 'max_value': 'Rainfall must be at most 300mm.'}
    )

    def clean(self):
        cleaned_data = super().clean()

        # Custom Validation Example (if needed)
        if cleaned_data['temperature'] > 30 and cleaned_data['humidity'] < 20:
            raise forms.ValidationError("Temperature above 30°C requires humidity above 20%.")

        return cleaned_data
