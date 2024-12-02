# Generated by Django 5.0.6 on 2024-05-25 09:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HDWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='published', max_length=50, verbose_name='Статус')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='HD-wallet name')),
                ('first_address', models.CharField(help_text='Wallet address for initial derivation path, Ex.: "m/44\'/60\'/0\'/0/0". Needed for identification HD-wallet', max_length=200, unique=True, verbose_name='First wallet address')),
                ('blockchain', models.CharField(blank=True, choices=[('solana', 'Solana'), ('bsc', 'Binance Smart Chain'), ('bnb', 'Binance Chain'), ('ton', 'Telegram Open Network')], max_length=20, verbose_name='Blockchain')),
                ('last_derivation_path', models.CharField(blank=True, max_length=100, verbose_name='Last derivation path')),
                ('user', models.ManyToManyField(related_name='hdwallets', to=settings.AUTH_USER_MODEL, verbose_name='HD-Wallet owners')),
            ],
            options={
                'verbose_name': 'HD-wallet',
                'verbose_name_plural': 'HD-wallets',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='published', max_length=50, verbose_name='Статус')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Wallet name')),
                ('wallet_address', models.CharField(max_length=200, unique=True, verbose_name='Wallet address')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Wallet description')),
                ('blockchain', models.CharField(blank=True, choices=[('solana', 'Solana'), ('bsc', 'Binance Smart Chain'), ('bnb', 'Binance Chain'), ('ton', 'Telegram Open Network')], max_length=20, verbose_name='Blockchain')),
                ('derivation_path', models.CharField(blank=True, max_length=100, verbose_name='Derivation path')),
                ('hd_wallet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_wallets', to='wallet.hdwallet', verbose_name='HD-Wallet')),
                ('user', models.ManyToManyField(related_name='wallets', to=settings.AUTH_USER_MODEL, verbose_name='Wallet owners')),
            ],
            options={
                'verbose_name': 'wallet',
                'verbose_name_plural': 'wallets',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='published', max_length=50, verbose_name='Статус')),
                ('transaction_id', models.CharField(max_length=200, unique=True, verbose_name='Transaction id')),
                ('sender', models.CharField(blank=True, max_length=200, verbose_name='Sender')),
                ('recipient', models.CharField(blank=True, max_length=200, verbose_name='Recipient')),
                ('pre_balances', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Pre-balances')),
                ('post_balances', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Post-balances')),
                ('transaction_time', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Transaction time')),
                ('slot', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Transaction slot')),
                ('transaction_status', models.CharField(blank=True, max_length=200, verbose_name='Transaction status')),
                ('transaction_err', models.CharField(blank=True, max_length=200, verbose_name='Transaction error')),
                ('wallet', models.ManyToManyField(related_name='transactions', to='wallet.wallet', verbose_name='Wallet')),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
                'ordering': ['transaction_time'],
            },
        ),
    ]