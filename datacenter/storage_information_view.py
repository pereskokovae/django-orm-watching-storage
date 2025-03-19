from datacenter.models import Passcard
from datacenter.models import Visit
from .helpers import format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    visits_active = Visit.objects.filter(leaved_at__isnull=True)

    for visit in visits_active:
        delta, entered_time = visit.get_duration()
        owner_name = visit.passcard.owner_name
        non_closed_visits.append({
            'who_entered': owner_name,
            'entered_at': entered_time,
            'duration': format_duration(delta),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)