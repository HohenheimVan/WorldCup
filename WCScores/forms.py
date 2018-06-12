from django import forms
from django.core.validators import EmailValidator
from django.forms import ModelForm

from WCScores.models import Team, UserScore


class AddTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['country', 'group', 'FIFA']



class AddMatchForm(forms.Form):
    datetime = forms.SplitDateTimeField(input_date_formats=['%d.%m.%Y'],
                                        input_time_formats=['%H:%M'],
                                        widget=forms.SplitDateTimeWidget(date_format='%d.%m.%Y',
                                                                         time_format='%H:%M'))
    team_1 = forms.ModelChoiceField(queryset=Team.objects.all())
    team_2 = forms.ModelChoiceField(queryset=Team.objects.all())


class InputScoresForm(forms.Form):
    team_1_score = forms.IntegerField(min_value=0, max_value=20)
    team_2_score = forms.IntegerField(min_value=0, max_value=20)


class UserScoresForm(forms.Form):
    team_1_score = forms.IntegerField(min_value=0, max_value=20)
    team_2_score = forms.IntegerField(min_value=0, max_value=20)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='user-name')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='password2')
    first_name = forms.CharField(label='first-name')
    last_name = forms.CharField(label='last-name')
    email = forms.CharField(label='user-email',
                            validators=[EmailValidator(message='zly email')])
