# Generated by Django 2.0.4 on 2018-05-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_auto_20180530_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hsgtcg',
            options={'verbose_name': '沪深港通持股'},
        ),
        migrations.AddField(
            model_name='hsgtcg',
            name='tradedate',
            field=models.DateField(default=None, verbose_name='日期'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hsgtcg',
            name='code',
            field=models.CharField(db_index=True, max_length=10, null=True, verbose_name='代码'),
        ),
        migrations.AlterUniqueTogether(
            name='hsgtcg',
            unique_together={('code', 'tradedate')},
        ),
    ]
