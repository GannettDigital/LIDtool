from django.core.mail import send_mail
from django.conf import settings
import os
from lid.models import Match
from django.core.management.base import BaseCommand, CommandError
import datetime

class Command(BaseCommand):
    args = 'None needed'
    help = 'Sends emails to reporters in each state that had new billmatches added today'

    def handle(self, *args, **options):
        today = datetime.date.today()
        matches = Match.objects.filter(timestamp__year=today.year) 
        subject = str(matches.count()) + ' new records added to LID today'
        message = 'Check them out at http://172.23.0.168:8000/lid/'
        email_from = 'USAT model bill detector'
        recipient_list = ['mwynn@usatoday.com', 'jkelly@usatoday.com', 'matt.wynn@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
