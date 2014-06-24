# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Bus.imei'
        db.delete_column(u'tracker_bus', 'imei')

        # Adding field 'Bus.imeib'
        db.add_column(u'tracker_bus', 'imeib',
                      self.gf('django.db.models.fields.CharField')(default=3243455454, max_length=25),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Bus.imei'
        db.add_column(u'tracker_bus', 'imei',
                      self.gf('django.db.models.fields.CharField')(default=1223435544545, max_length=25),
                      keep_default=False)

        # Deleting field 'Bus.imeib'
        db.delete_column(u'tracker_bus', 'imeib')


    models = {
        u'tracker.bus': {
            'Meta': {'object_name': 'Bus'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imeib': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'license_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Route']"})
        },
        u'tracker.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tracker.coordinate': {
            'Meta': {'object_name': 'coordinate'},
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Bus']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'tracker.route': {
            'Meta': {'object_name': 'Route'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_end': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'route_start': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'tracker.route_stop': {
            'Meta': {'object_name': 'Route_Stop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stops'", 'to': u"orm['tracker.Route']"}),
            'stop_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['tracker']