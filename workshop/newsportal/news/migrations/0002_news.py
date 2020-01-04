# Generated by Django 3.0.2 on 2020-01-04 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='news/')),
                ('taglist', models.TextField()),
                ('date', models.DateField()),
                ('newscategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewCategory')),
            ],
        ),
    ]