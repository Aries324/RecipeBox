# Generated by Django 3.0.5 on 2020-06-04 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favorite',
            field=models.ManyToManyField(to='recipes.Recipe'),
        ),
    ]
