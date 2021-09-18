from django.shortcuts import render, redirect
# Create your views here.
from .models import Meetup, Participants
from .forms import RegistrationForm


def index(request):
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


# <slag:meetup_slug> part we mention in url page, we have to use meetup_slug part as attribute in our definition.
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participants.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
            })
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False
        })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })
