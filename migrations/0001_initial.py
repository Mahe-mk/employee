# Generated by Django 4.1.1 on 2022-11-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeeapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empNo', models.IntegerField()),
                ('empName', models.CharField(max_length=20)),
                ('empSalary', models.IntegerField()),
                ('empAddress', models.CharField(max_length=100)),
                ('empPhoto', models.ImageField(upload_to='office/image/')),
            ],
        ),
    ]
