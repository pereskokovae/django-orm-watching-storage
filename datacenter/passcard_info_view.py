from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .helpers import is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = Visit.objects.filter(passcard=passcard)
    formatted_visits = []
    
    for visit in this_passcard_visits:
        delta, entered_time = visit.get_duration()
        is_strange = is_visit_long(visit)
        formatted_visit = {
                'entered_at': entered_time.strftime('%Y-%m-%d %H:%M:%S'),
                'duration': delta,
                'is_strange': is_strange
                }
        formatted_visits.append(formatted_visit)


    context = {
        'passcard': passcard,
        'this_passcard_visits': formatted_visits
    }
    return render(request, 'passcard_info.html', context)