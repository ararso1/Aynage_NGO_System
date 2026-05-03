import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aynage_app', '0015_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(
                blank=True,
                null=True,
                upload_to='videos/',
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=['mp4', 'webm', 'ogg', 'mov']
                    )
                ],
            ),
        ),
    ]
