import csv
import os
from config.settings import MEDIA_DIR
from django.core.management.base import BaseCommand, CommandError
from apps.musics.models import Music
from apps.right_owners.models import RightOwner


def create_generator(file_path):
    with open(file_path, "r", encoding='UTF-8') as csv_file:
        data_reader = csv.DictReader(csv_file)
        # first_row = next(data_reader)
        for row in data_reader:
            yield row  # yield the header row


def parse():
    pass


class Command(BaseCommand):
    help = 'Closes the specified Music for voting'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        filename = options.get('file_path')
        file_path = os.path.join(MEDIA_DIR, filename[0])
        print(file_path)
        print('hola command')
        id_society = []
        read_file = create_generator(file_path)
        music = Music()
        right_owner = RightOwner()
        for row in read_file:
            right_owner.name = row['RIGHT OWNER']
            right_owner.role = row['ROLE']
            right_owner.ipi = row['IPI NUMBER']
            right_owner.save()
            if not row['ID SOCIETY'] in id_society:
                id_society.append(row['ID SOCIETY'])
                music._id = row['ID SOCIETY']
                music.iswc = row['ISWC']
                music.original_title = row['ORIGINAL TITLE']
                music.alternative_title_1 = row['ALTERNATIVE TITLE 1']
                music.alternative_title_2 = row[' ALTERNATIVE TITLE 2']
                music.alternative_title_3 = row['ALTERNATIVE TITLE 3']
                music.save()
                music = Music()  
            right_owner = RightOwner()        
            print(row)
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Music.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
