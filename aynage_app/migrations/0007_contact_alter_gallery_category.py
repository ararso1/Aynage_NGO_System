# Generated by Django 5.1.7 on 2025-03-27 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynage_app', '0006_gallery_alter_blog_banner_alter_blog_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=455)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.CharField(choices=[('certifications', 'Certifications and Banners')], max_length=100),
        ),
    ]
