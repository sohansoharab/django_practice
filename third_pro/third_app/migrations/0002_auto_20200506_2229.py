# Generated by Django 3.0.6 on 2020-05-06 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='UserPage',
        ),
        migrations.CreateModel(
            name='Indexes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frst_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='third_app.UserPage')),
            ],
        ),
    ]