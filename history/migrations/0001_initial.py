# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import history.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('symbol', models.CharField(max_length=30)),
                ('coin_balance', models.FloatField()),
                ('usd_balance', models.FloatField(null=True)),
                ('btc_balance', models.FloatField()),
                ('exchange_to_btc_rate', models.FloatField()),
                ('exchange_to_usd_rate', models.FloatField(null=True)),
                ('deposited_amount_usd', models.FloatField(default=0.0)),
                ('deposited_amount_btc', models.FloatField(default=0.0)),
                ('date_str', models.CharField(default='0', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassifierTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('type', models.CharField(default='mock', max_length=30)),
                ('symbol', models.CharField(max_length=30)),
                ('name', models.CharField(default='', max_length=100)),
                ('datasetinputs', models.IntegerField()),
                ('granularity', models.IntegerField()),
                ('minutes_back', models.IntegerField(default=0)),
                ('timedelta_back_in_granularity_increments', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('prediction_size', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('output', models.TextField()),
                ('percent_correct', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('symbol', models.CharField(max_length=30)),
                ('amount', models.FloatField(null=True)),
                ('type', models.CharField(max_length=10)),
                ('txid', models.CharField(default='', max_length=500)),
                ('status', models.CharField(default='none', max_length=100)),
                ('created_on_str', models.CharField(default='', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PerformanceComp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('symbol', models.CharField(max_length=30)),
                ('nn_rec', models.FloatField()),
                ('actual_movement', models.FloatField()),
                ('delta', models.FloatField()),
                ('created_on_str', models.CharField(max_length=30)),
                ('directionally_same', models.BooleanField(default=False)),
                ('directionally_same_int', models.IntegerField(default=0)),
                ('weighted_avg_nn_rec', models.FloatField(default=0)),
                ('pct_buy', models.FloatField(default=0)),
                ('pct_hold', models.FloatField(default=0)),
                ('pct_sell', models.FloatField(default=0)),
                ('rec_count', models.IntegerField(default=0)),
                ('price_timerange_start', models.DateTimeField(default=None, null=True)),
                ('price_timerange_end', models.DateTimeField(default=None, null=True)),
                ('tr_timerange_start', models.DateTimeField(default=None, null=True)),
                ('tr_timerange_end', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PredictionTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('type', models.CharField(default='mock', max_length=30)),
                ('symbol', models.CharField(max_length=30)),
                ('percent_correct', models.FloatField(null=True)),
                ('avg_diff', models.FloatField(null=True)),
                ('datasetinputs', models.IntegerField()),
                ('hiddenneurons', models.IntegerField()),
                ('granularity', models.IntegerField()),
                ('minutes_back', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('epochs', models.IntegerField(default=0)),
                ('prediction_size', models.IntegerField(default=0)),
                ('learningrate', models.FloatField(default=0)),
                ('momentum', models.FloatField(default=0)),
                ('weightdecay', models.FloatField(default=0)),
                ('bias', models.BooleanField(default=False)),
                ('bias_chart', models.IntegerField(default=-1)),
                ('recurrent', models.BooleanField(default=False)),
                ('recurrent_chart', models.IntegerField(default=-1)),
                ('profitloss', models.FloatField(default=0)),
                ('profitloss_int', models.IntegerField(default=0)),
                ('timedelta_back_in_granularity_increments', models.IntegerField(default=0)),
                ('output', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('symbol', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('volume', models.FloatField(null=True)),
                ('lowestask', models.FloatField(null=True)),
                ('highestbid', models.FloatField(null=True)),
                ('created_on_str', models.CharField(default='', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('symbol', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('amount', models.FloatField(null=True)),
                ('type', models.CharField(max_length=10)),
                ('response', models.TextField()),
                ('orderNumber', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='none', max_length=10)),
                ('net_amount', models.FloatField(null=True)),
                ('created_on_str', models.CharField(default='', max_length=50)),
                ('fee_amount', models.FloatField(null=True)),
                ('btc_amount', models.FloatField(null=True)),
                ('usd_amount', models.FloatField(null=True)),
                ('btc_fee_amount', models.FloatField(null=True)),
                ('usd_fee_amount', models.FloatField(null=True)),
                ('opposite_price', models.FloatField(null=True)),
                ('net_profit', models.FloatField(null=True)),
                ('btc_net_profit', models.FloatField(null=True)),
                ('usd_net_profit', models.FloatField(null=True)),
                ('opposite_trade', models.ForeignKey(to='history.Trade', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TradeRecommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=history.models.get_time)),
                ('modified_on', models.DateTimeField(default=history.models.get_time)),
                ('symbol', models.CharField(max_length=30)),
                ('made_on', models.TextField(max_length=30)),
                ('recommendation', models.CharField(max_length=30)),
                ('confidence', models.FloatField()),
                ('created_on_str', models.CharField(default='', max_length=30)),
                ('net_amount', models.FloatField(default=0)),
                ('clf', models.ForeignKey(to='history.ClassifierTest', null=True)),
                ('made_by', models.ForeignKey(to='history.PredictionTest', null=True)),
                ('trade', models.ForeignKey(to='history.Trade', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
