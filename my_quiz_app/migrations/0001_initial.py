# Generated by Django 3.2 on 2021-05-07 13:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('for_which_quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_quiz_app.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('for_which_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_quiz_app.question')),
            ],
        ),
    ]
