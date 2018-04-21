# Generated by Django 2.0.4 on 2018-04-21 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000, unique=True)),
                ('date_added', models.DateField(blank=True, null=True)),
                ('date_updated', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=500)),
                ('alexa_rank', models.IntegerField()),
                ('date_added', models.DateField(blank=True, null=True)),
                ('date_updated', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('date_added', models.DateField(blank=True, null=True)),
                ('date_updated', models.DateField(blank=True, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='website',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webSitesApp.WebsiteCategory'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webSitesApp.Website'),
        ),
    ]