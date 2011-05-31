# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SyncedObject'
        db.create_table('django_storymarket_syncedobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='storymarket_synced_objects', to=orm['contenttypes.ContentType'])),
            ('object_pk', self.gf('django.db.models.fields.TextField')()),
            ('storymarket_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('storymarket_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('org', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('category', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('pricing', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('rights', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('django_storymarket', ['SyncedObject'])

        # Adding model 'AutoSyncedModel'
        db.create_table('django_storymarket_autosyncedmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='storymarket_autosynced_models', to=orm['contenttypes.ContentType'])),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('django_storymarket', ['AutoSyncedModel'])

        # Adding model 'AutoSyncRule'
        db.create_table('django_storymarket_autosyncrule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sync_model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rules', to=orm['django_storymarket.AutoSyncedModel'])),
            ('include', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('op', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('django_storymarket', ['AutoSyncRule'])


    def backwards(self, orm):
        
        # Deleting model 'SyncedObject'
        db.delete_table('django_storymarket_syncedobject')

        # Deleting model 'AutoSyncedModel'
        db.delete_table('django_storymarket_autosyncedmodel')

        # Deleting model 'AutoSyncRule'
        db.delete_table('django_storymarket_autosyncrule')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'django_storymarket.autosyncedmodel': {
            'Meta': {'object_name': 'AutoSyncedModel'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'storymarket_autosynced_models'", 'to': "orm['contenttypes.ContentType']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'django_storymarket.autosyncrule': {
            'Meta': {'object_name': 'AutoSyncRule'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'op': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sync_model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rules'", 'to': "orm['django_storymarket.AutoSyncedModel']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'django_storymarket.syncedobject': {
            'Meta': {'object_name': 'SyncedObject'},
            'category': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'storymarket_synced_objects'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'object_pk': ('django.db.models.fields.TextField', [], {}),
            'org': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pricing': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rights': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'storymarket_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'storymarket_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['django_storymarket']
