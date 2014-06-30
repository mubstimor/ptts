# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'tracker_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tracker', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'tracker_contact')


    models = {
        u'tracker.bus': {
            'Meta': {'object_name': 'Bus'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imeib': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'license_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'route_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Route']", 'null': 'True', 'blank': 'True'})
        },
        u'tracker.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'tracker.coordinate': {
            'Meta': {'object_name': 'coordinate'},
            'bus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Bus']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Route']", 'null': 'True', 'blank': 'True'})
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