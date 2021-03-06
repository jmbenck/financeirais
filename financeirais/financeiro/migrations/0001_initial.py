# Generated by Django 3.1.1 on 2020-09-23 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('tipo', models.IntegerField(choices=[(1, 'Entrada'), (2, 'Saida')])),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='anexos/%Y/%m/')),
                ('descricao', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
    ]
