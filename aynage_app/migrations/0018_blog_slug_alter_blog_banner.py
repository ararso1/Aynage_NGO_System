from django.db import migrations, models
from django.utils.text import slugify


def populate_blog_slugs(apps, schema_editor):
    Blog = apps.get_model('aynage_app', 'Blog')
    used_slugs = set()

    for blog in Blog.objects.order_by('id'):
        base_slug = slugify(blog.title) or f"blog-{blog.pk}"
        base_slug = base_slug[:255]
        slug = base_slug
        counter = 1

        while slug in used_slugs or Blog.objects.filter(slug=slug).exclude(pk=blog.pk).exists():
            counter += 1
            suffix = f"-{counter}"
            slug = f"{base_slug[:255 - len(suffix)]}{suffix}"

        blog.slug = slug
        blog.save(update_fields=['slug'])
        used_slugs.add(slug)


class Migration(migrations.Migration):

    dependencies = [
        ('aynage_app', '0017_alter_blog_added_by_alter_blog_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.RunPython(populate_blog_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
