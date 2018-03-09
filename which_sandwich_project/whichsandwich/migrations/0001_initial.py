# Generated by Django 2.0.2 on 2018-03-09 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('calories', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('likes', models.PositiveIntegerField(blank=True)),
                ('dislikes', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Sandwiches',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('favourites', models.ManyToManyField(to='whichsandwich.Sandwich')),
            ],
        ),
        migrations.AddField(
            model_name='sandwich',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='whichsandwich.User'),
        ),
        migrations.AddField(
            model_name='sandwich',
            name='ingredients',
            field=models.ManyToManyField(to='whichsandwich.Ingredient'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sandwich',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='whichsandwich.Sandwich'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='whichsandwich.User'),
        ),
    ]
