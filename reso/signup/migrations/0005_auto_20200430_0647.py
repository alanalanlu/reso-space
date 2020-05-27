# Generated by Django 2.2.1 on 2020-04-30 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_user_chosen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='signup.Squad'),
        ),
    ]