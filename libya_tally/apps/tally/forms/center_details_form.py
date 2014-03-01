from django import forms
from django.utils.translation import ugettext as _

from libya_tally.apps.tally.models.center import Center
from libya_tally.libs.validators import MinLengthValidator


disable_copy_input = {
    'onCopy': 'return false;',
    'onDrag': 'return false;',
    'onDrop': 'return false;',
    'onPaste': 'return false;',
    'autocomplete': 'off',
    'class': 'form-control'
}
min_station_value = 1
max_station_value = 53


class CenterDetailsForm(forms.Form):
    validators = [MinLengthValidator(5)]
    center_error_messages = {
        'invalid': _(u"Expecting only numbers for center number")}

    center_number = forms.IntegerField(
        error_messages=center_error_messages,
        validators=validators,
        widget=forms.NumberInput(attrs=disable_copy_input),
        label=_(u"Center Number"))
    center_number_copy = forms.IntegerField(
        error_messages=center_error_messages,
        validators=validators,
        widget=forms.NumberInput(attrs=disable_copy_input),
        label=_(u"Center Number Copy"))
    station_number = forms.IntegerField(min_value=min_station_value,
                                        max_value=max_station_value,
                                        widget=forms.TextInput(
                                            attrs=disable_copy_input),
                                        label=_(u"Station Number"))
    station_number_copy = forms.IntegerField(min_value=min_station_value,
                                             max_value=max_station_value,
                                             widget=forms.TextInput(
                                                 attrs=disable_copy_input),
                                             label=_(u"Station Number Copy"))

    def __init__(self, *args, **kwargs):
        super(CenterDetailsForm, self).__init__(*args, **kwargs)
        self.fields['center_number'].widget.attrs['autofocus'] = 'on'

    def clean(self):
        """Ensure that the center number and center number copy match, as well
        as the station number and station number copy.  Also validate that the
        center number is a valid center number and that the station number is
        for a station in that center.
        """
        if self.is_valid():
            cleaned_data = super(CenterDetailsForm, self).clean()
            center_number = cleaned_data.get('center_number')
            center_number_copy = cleaned_data.get('center_number_copy')
            station_number = cleaned_data.get('station_number')
            station_number_copy = cleaned_data.get('station_number_copy')

            if center_number != center_number_copy:
                raise forms.ValidationError(_(u"Center Numbers do not match"))

            if station_number != station_number_copy:
                raise forms.ValidationError(_(u"Station Numbers do not match"))

            try:
                center = Center.objects.get(code=center_number)
                valid_station_numbers = [
                    d.values()[0] for d in
                    center.stations.values('station_number')]

                if not int(station_number) in valid_station_numbers:
                    raise forms.ValidationError(_(
                        u"Invalid Station Number for this Center"))

            except Center.DoesNotExist:
                raise forms.ValidationError(_(u"Center Number does not exist"))

            return cleaned_data
