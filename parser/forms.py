from django import forms
from . import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Pictures', 'Pictures'),

    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Pictures':
            geo_parser = parser.parser()
            for i in geo_parser:
                models.TvParser.objects.create(**i)