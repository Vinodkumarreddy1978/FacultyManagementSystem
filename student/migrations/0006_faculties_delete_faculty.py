# Generated by Django 4.1.3 on 2022-11-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_rename_faculty_achievements_faculty_achievements_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='media')),
                ('Subject', models.CharField(max_length=49)),
                ('Experience', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Qualification', models.CharField(max_length=48)),
                ('Achievements', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=40)),
                ('Mobile_Number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='faculty',
        ),
    ]