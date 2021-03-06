# Generated by Django 3.0.1 on 2020-01-22 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shs_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Body', models.CharField(max_length=10000)),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shs_website.Title')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='Body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shs_website.Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shs_website.Title'),
        ),
    ]
