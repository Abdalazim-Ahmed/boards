# Generated by Django 4.2.5 on 2023-11-13 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_post_topic_alter_topic_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board'),
        ),
    ]
