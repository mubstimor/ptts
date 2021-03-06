# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Route'
        db.create_table(u'tracker_route', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('route_start', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('route_end', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'tracker', ['Route'])

        # Adding model 'Buse'
        db.create_table(u'tracker_buse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('imeib', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('route_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.Route'], null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'tracker', ['Buse'])

        # Adding model 'Stop'
        db.create_table(u'tracker_stop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stops', to=orm['tracker.Route'])),
        ))
        db.send_create_signal(u'tracker', ['Stop'])

        # Adding model 'coordinate'
        db.create_table(u'tracker_coordinate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('speed', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('route_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.Route'], null=True, blank=True)),
            ('bus_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tracker.Buse'], null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'tracker', ['coordinate'])

        # Adding model 'Contact'
        db.create_table(u'tracker_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'tracker', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Route'
        db.delete_table(u'tracker_route')

        # Deleting model 'Buse'
        db.delete_table(u'tracker_buse')

        # Deleting model 'Stop'
        db.delete_table(u'tracker_stop')

        # Deleting model 'coordinate'
        db.delete_table(u'tracker_coordinate')

        # Deleting model 'Contact'
        db.delete_table(u'tracker_contact')


    models = {
        u'tracker.buse': {
            'Meta': {'object_name': 'Buse'},
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
            'bus_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Buse']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tracker.Route']", 'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'tracker.route': {
            'Meta': {'object_name': 'Route'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_end': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'route_start': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'tracker.stop': {
            'Meta': {'object_name': 'Stop'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stops'", 'to': u"orm['tracker.Route']"}),
            'stop_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['tracker']