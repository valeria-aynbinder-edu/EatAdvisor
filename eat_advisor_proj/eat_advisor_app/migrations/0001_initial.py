# Generated by Django 3.2.12 on 2022-02-09 10:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('type', models.CharField(blank=True, max_length=128, null=True)),
                ('price_range', models.PositiveSmallIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('pic_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traveler_type', models.CharField(blank=True, choices=[('FAMILIES', 'families'), ('COUPLES', 'Couples'), ('SOLO', 'Solo'), ('BUSINESS', 'Business'), ('FRIENDS', 'Friends')], max_length=64, null=True)),
                ('stars', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('date', models.DateField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='eat_advisor_app.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='reviewers',
            field=models.ManyToManyField(through='eat_advisor_app.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]