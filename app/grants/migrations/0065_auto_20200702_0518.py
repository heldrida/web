# Generated by Django 2.2.4 on 2020-07-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0064_auto_20200629_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='sybil_score',
            field=models.DecimalField(decimal_places=4, default=0, help_text='The Grants Sybil Score', max_digits=50),
        ),
        migrations.AddField(
            model_name='grant',
            name='weighted_risk_score',
            field=models.DecimalField(decimal_places=4, default=0, help_text='The Grants Weighted Risk Score', max_digits=50),
        ),
        migrations.AlterField(
            model_name='grant',
            name='grant_type',
            field=models.CharField(choices=[('tech', 'tech'), ('health', 'health'), ('media', 'Community'), ('change', 'change'), ('matic', 'matic')], db_index=True, default='tech', help_text='Grant CLR category', max_length=15),
        ),
    ]