# Generated by Django 5.1.1 on 2024-10-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_overview', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
