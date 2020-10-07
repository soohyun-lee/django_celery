# Generated by Django 3.1.2 on 2020-10-06 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='introduce_image',
        ),
        migrations.RemoveField(
            model_name='products',
            name='introduce_text',
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction_image', models.CharField(max_length=500)),
                ('introduction_text', models.CharField(max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
            options={
                'db_table': 'Introduction',
            },
        ),
    ]
