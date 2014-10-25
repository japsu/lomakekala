# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=63)),
                ('slug', models.CharField(unique=True, max_length=63)),
                ('code', models.CharField(max_length=255)),
                ('is_public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormHandler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('form', models.ForeignKey(to='lomakekala.Form')),
            ],
            options={
                'ordering': ('form', 'order'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=63)),
                ('slug', models.CharField(unique=True, max_length=63)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HandlerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=63)),
                ('slug', models.CharField(unique=True, max_length=63)),
                ('code', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailHandler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_address', models.CharField(max_length=255, blank=True)),
                ('subject_template', models.CharField(max_length=1023)),
                ('body_template', models.TextField()),
                ('handler', models.OneToOneField(to='lomakekala.Handler')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailHandlerRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=255, blank=True)),
                ('email_address', models.CharField(max_length=255)),
                ('recipient_type', models.CharField(default=b'to', max_length=3, choices=[(b'to', b'To'), (b'cc', b'CC'), (b'bcc', b'BCC')])),
                ('mail_handler', models.ForeignKey(to='lomakekala.MailHandler')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='handler',
            name='handler_type',
            field=models.ForeignKey(to='lomakekala.HandlerType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formhandler',
            name='handler',
            field=models.ForeignKey(to='lomakekala.Handler'),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='formhandler',
            index_together=set([('form', 'order', 'handler')]),
        ),
    ]
