from django.core.management.base import BaseCommand
from apps.bot.main_bot import main


class Command(BaseCommand):
    # comando start bot
    help = 'start bot'

    def handle(self, *args, **kwargs):
        main()
