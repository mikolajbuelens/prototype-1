# Generated by Django 5.1.1 on 2024-10-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_overview', '0003_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='static/images/'),
        ),
    ]
