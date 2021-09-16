from django.shortcuts import render
# Create your views here.
from .models import Meetup


def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


# <slag:meetup_slug> part we mention in url page, we have to use meetup_slug part as attribute in our definition.
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description
        })
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False
        })

