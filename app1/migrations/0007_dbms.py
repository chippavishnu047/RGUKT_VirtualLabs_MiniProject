# Generated by Django 4.1.7 on 2023-07-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_question_alter_res_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
