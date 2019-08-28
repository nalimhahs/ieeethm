# Generated by Django 2.2.4 on 2019-08-28 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField(max_length=30)),
                ('razorpay_order_id', models.TextField(max_length=50)),
                ('razorpay_payment_id', models.TextField(max_length=50, null=True)),
                ('razorpay_signature', models.TextField(max_length=50, null=True)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=7)),
                ('entity', models.TextField(max_length=10)),
                ('reciept', models.TextField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.User')),
            ],
        ),
    ]
