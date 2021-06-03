# Generated by Django 2.2.12 on 2021-06-03 18:05

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fase3new_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Fase3NEW_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fase3new_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Fase3NEW_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('rHL_1', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_2', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_3', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_4', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_5', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_6', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_7', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_8', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_9', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_10', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_11', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL_12', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('rHL', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Fase3NEW.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fase3new_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fase3new_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fase3NEW.Subsession')),
            ],
            options={
                'db_table': 'Fase3NEW_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fase3NEW.Subsession'),
        ),
    ]
