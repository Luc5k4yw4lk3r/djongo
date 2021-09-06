from django.core.management.base import BaseCommand, CommandError
from apps.musics.models import Music
import csv
import os
from config.settings import MEDIA_DIR


def create_generator(file_path):
    with open(file_path, "r", encoding='latin1') as csv_file:
        data_reader = csv.reader(csv_file)
        # self.columns = next(data_reader)
        for row in data_reader:
            yield row  # yield the header row


class Command(BaseCommand):
    help = 'Closes the specified Music for voting'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        filename = options.get('file_path')
        file_path = os.path.join(MEDIA_DIR, filename[0])
        print(file_path)
        print('hola command')
        read_file = create_generator(file_path)
        for row in read_file:
            print(row)
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Music.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
