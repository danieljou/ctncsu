# Generated by Django 4.2.2 on 2023-07-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_article_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='contetu',
        ),
        migrations.AddField(
            model_name='article',
            name='Titre',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]