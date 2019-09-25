from django_cron import CronJobBase, Schedule
from django.core import mail
from django.core.mail import BadHeaderError, send_mail, EmailMessage


class MyCronJob(CronJobBase):
    #RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=1)
    #schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'scraperamazone.MyCronJob'

    def do(self):
        print('')
