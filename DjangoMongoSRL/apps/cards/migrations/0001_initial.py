# Generated by Django 3.0.5 on 2021-09-04 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='Card name')),
                ('answer', models.TextField(help_text='Card name')),
                ('value', models.IntegerField(blank=True, help_text='Number of card', null=True)),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.Deck')),
            ],
        ),
    ]
