# Burada veri tabanı işlemlerimiz gerçekleşiyor. Veri tabanında tutulacak veriler ve özellikleri ekleniyor.

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('sub', models.CharField(choices=[('SL', 'Sales'), ('BY', 'Buying'), ('MG', 'Management'), ('BG', 'Budget')], default='BG', max_length=2)),
            ],
        ),
    ]
