from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(visit):
        entered_time = timezone.localtime(visit.entered_at)
        if visit.leaved_at:
            leaved_time = timezone.localtime(visit.leaved_at)
        else:
            leaved_time = timezone.localtime(timezone.now())
        delta = leaved_time - entered_time
        owner_name = visit.passcard.owner_name
        return delta, owner_name, entered_time
    
    def is_visit_long(visit, minutes=60):
        delta, _, _ = visit.get_duration()
        duration = delta.total_seconds() / 60
        if duration > minutes:
            return False
        else:
            return True

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
