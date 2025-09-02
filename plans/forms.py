from django import forms
from .models import Task
from datetime import timedelta
import re

class TaskForm(forms.ModelForm):
    duration_input = forms.CharField(
        required=True,
        label="Estimated duration",
        help_text="Example: 2 days 3 hours or 1h 30m"
    )

    class Meta:
        model = Task
        fields = ['content', 'is_done', 'tags']  # deadline excluded

    def clean_duration_input(self):
        raw = self.cleaned_data['duration_input'].lower()
        days = hours = minutes = 0

        # Match patterns like "2 days", "3 hours", "45 minutes"
        day_match = re.search(r'(\d+)\s*d(ays)?', raw)
        hour_match = re.search(r'(\d+)\s*h(ours)?', raw)
        minute_match = re.search(r'(\d+)\s*m(inutes)?', raw)

        if day_match:
            days = int(day_match.group(1))
        if hour_match:
            hours = int(hour_match.group(1))
        if minute_match:
            minutes = int(minute_match.group(1))

        return timedelta(days=days, hours=hours, minutes=minutes)