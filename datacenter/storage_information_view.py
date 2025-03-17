from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    def format_duration(delta):
        seconds = delta.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}ч {minutes}мин"

    non_closed_visits = []
    visits_active = Visit.objects.filter(leaved_at__isnull=True)

    for visit in visits_active:
        delta, owner_name, entered_time = visit.get_duration()
        non_closed_visits.append({
            'who_entered': owner_name,
            'entered_at': entered_time,
            'duration': format_duration(delta),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)