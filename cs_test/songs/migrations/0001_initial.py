from django.db import migrations, models
import django.db.models.deletion


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='1'
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="songs",
                        to="songs.artist",
                    ),
                ),
            ],
        ),
        migrations.RunPython(create_superuser),
    ]
