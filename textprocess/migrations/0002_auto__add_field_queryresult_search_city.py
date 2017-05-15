# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'QueryResult.search_city'
        db.add_column(u'textprocess_queryresult', 'search_city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=3, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'QueryResult.search_city'
        db.delete_column(u'textprocess_queryresult', 'search_city')


    models = {
        u'textprocess.queryresult': {
            'Meta': {'object_name': 'QueryResult'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_post_data': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {}),
            'results': ('django.db.models.fields.TextField', [], {}),
            'search_city': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'submitted_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['textprocess']