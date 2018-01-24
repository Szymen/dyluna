from django import forms
from ..models.Workshop_ScheduleModel import Workshop_Schedule


class WorkshopSchedulesForm(forms.ModelForm):

    class Meta:
        model = Workshop_Schedule
        exclude = ()