# Generated by Django 5.2.3 on 2025-06-23 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milkmain', '0002_milkuser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('unpaid', 'Unpaid')], default='paid', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='milkmain.milkuser')),
            ],
        ),
    ]
