from django.core.mail import send_mail
from django.template.loader import render_to_string
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
        matches = Match.objects.filter(timestamp__year=today.year, timestamp__month=today.month, timestamp__day=today.day)
        if matches.count() > 0:
            recipient_list = ['mwynn@usatoday.com', 'jkelly@usatoday.com', 'matt.wynn@gmail.com']
            msg_plain = render_to_string('lidemail.txt', {'matches': matches})
            msg_html = render_to_string('lidemail.html', {'matches': matches})
            send_mail('New model bills detected',msg_plain,'USAT model bill detector',recipient_list,html_message=msg_html,)
