# Generated by Django 4.0 on 2022-01-14 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election_results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Polling_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.CharField(blank=True, max_length=5, null=True)),
                ('party_score', models.IntegerField()),
                ('polling_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='election_results.pollingunit')),
            ],
        ),
    ]