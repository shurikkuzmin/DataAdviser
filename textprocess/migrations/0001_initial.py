# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QueryResult'
        db.create_table(u'textprocess_queryresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submitted_text', self.gf('django.db.models.fields.TextField')()),
            ('results', self.gf('django.db.models.fields.TextField')()),
            ('http_post_data', self.gf('django.db.models.fields.TextField')()),
            ('metadata', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'textprocess', ['QueryResult'])


    def backwards(self, orm):
        # Deleting model 'QueryResult'
        db.delete_table(u'textprocess_queryresult')


    models = {
        u'textprocess.queryresult': {
            'Meta': {'object_name': 'QueryResult'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_post_data': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {}),
            'results': ('django.db.models.fields.TextField', [], {}),
            'submitted_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['textprocess']