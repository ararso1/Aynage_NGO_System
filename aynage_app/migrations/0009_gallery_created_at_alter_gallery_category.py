# Generated by Django 5.1.7 on 2025-03-31 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynage_app', '0008_category_remove_blog_category_blog_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.CharField(choices=[('certifications', 'Certifications'), ('early_child_development', 'Early Child Development'), ('basic_educations', 'Basic Education'), ('youth_Development', 'Youth Development'), ('community_empowerment', 'Community Empowerment')], max_length=100),
        ),
    ]
