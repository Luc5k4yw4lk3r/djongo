import csv
import os
from config.settings import MEDIA_DIR
from django.core.management.base import BaseCommand, CommandError
from apps.musics.models import Music, Title
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
        id_society = []
        read_file = create_generator(file_path)
        music = Music()
        right_owner = RightOwner()
        right_owner_lst = []
        title = Title()
        titles = []
        last_music = ''
        prev_music_id = ''
        prev_music_iswc = ''
        prev_original_title = ''
        prev_alternative_title_1 = ''
        prev_alternative_title_2 = ''
        prev_alternative_title_3 = ''
        for row in read_file:
            if not last_music:
                last_music = row['ID SOCIETY']
            if last_music != row['ID SOCIETY']:
                last_music = row['ID SOCIETY']
                music = Music(id_society=prev_music_id, iswc=prev_music_iswc)
                music.save()
                if prev_original_title != '':
                    title_tmp = Title(title=prev_original_title, type='Original Title')
                    title_tmp.music = music
                    title_tmp.save()
                    # music.entry_set.add(title_tmp)
                if prev_alternative_title_1 != '':
                    title_tmp = Title(title=prev_alternative_title_1, type='Alternative Title 1')
                    title_tmp.music = music
                    title_tmp.save()
                if prev_alternative_title_2 != '':
                    title_tmp = Title(title=prev_alternative_title_2, type='Alternative Title 2')
                    title_tmp.music = music
                    title_tmp.save()
                if prev_alternative_title_3 != '':
                    title_tmp = Title(title=prev_alternative_title_3, type='Alternative Title 3')
                    title_tmp.music = music
                    title_tmp.save()
                for r_owner in right_owner_lst:
                    music.right_owner.add(r_owner)
                # music.save()
                right_owner_lst = []
            right_owner.name = row['RIGHT OWNER']
            right_owner.role = row['ROLE']
            right_owner.ipi = row['IPI NUMBER']
            right_owner.save()
            right_owner_lst.append(right_owner)

            # if not row['ID SOCIETY'] in id_society:
                # id_society.append(row['ID SOCIETY'])
            prev_music_id = row['ID SOCIETY']
            prev_music_iswc = row['ISWC']
            prev_original_title = row['ORIGINAL TITLE']
            prev_alternative_title_1 = row['ALTERNATIVE TITLE 1']
            prev_alternative_title_2 = row[' ALTERNATIVE TITLE 2']
            prev_alternative_title_3 = row['ALTERNATIVE TITLE 3']
            # music.save()
            # music = Music()  
            right_owner = RightOwner()        
            # print(row)