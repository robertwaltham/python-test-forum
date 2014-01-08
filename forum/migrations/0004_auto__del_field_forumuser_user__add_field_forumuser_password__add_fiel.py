# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ForumUser.user'
        db.delete_column(u'forum_forumuser', 'user_id')

        # Adding field 'ForumUser.password'
        db.add_column(u'forum_forumuser', 'password',
                      self.gf('django.db.models.fields.CharField')(default=1234, max_length=128),
                      keep_default=False)

        # Adding field 'ForumUser.last_login'
        db.add_column(u'forum_forumuser', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'ForumUser.is_superuser'
        db.add_column(u'forum_forumuser', 'is_superuser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ForumUser.email'
        db.add_column(u'forum_forumuser', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', unique=True, max_length=254),
                      keep_default=False)

        # Adding field 'ForumUser.first_name'
        db.add_column(u'forum_forumuser', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'ForumUser.last_name'
        db.add_column(u'forum_forumuser', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'ForumUser.is_staff'
        db.add_column(u'forum_forumuser', 'is_staff',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ForumUser.is_active'
        db.add_column(u'forum_forumuser', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ForumUser.date_joined'
        db.add_column(u'forum_forumuser', 'date_joined',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding M2M table for field groups on 'ForumUser'
        m2m_table_name = db.shorten_name(u'forum_forumuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('forumuser', models.ForeignKey(orm[u'forum.forumuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['forumuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'ForumUser'
        m2m_table_name = db.shorten_name(u'forum_forumuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('forumuser', models.ForeignKey(orm[u'forum.forumuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['forumuser_id', 'permission_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ForumUser.user'
        raise RuntimeError("Cannot reverse this migration. 'ForumUser.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ForumUser.user'
        db.add_column(u'forum_forumuser', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'ForumUser.password'
        db.delete_column(u'forum_forumuser', 'password')

        # Deleting field 'ForumUser.last_login'
        db.delete_column(u'forum_forumuser', 'last_login')

        # Deleting field 'ForumUser.is_superuser'
        db.delete_column(u'forum_forumuser', 'is_superuser')

        # Deleting field 'ForumUser.email'
        db.delete_column(u'forum_forumuser', 'email')

        # Deleting field 'ForumUser.first_name'
        db.delete_column(u'forum_forumuser', 'first_name')

        # Deleting field 'ForumUser.last_name'
        db.delete_column(u'forum_forumuser', 'last_name')

        # Deleting field 'ForumUser.is_staff'
        db.delete_column(u'forum_forumuser', 'is_staff')

        # Deleting field 'ForumUser.is_active'
        db.delete_column(u'forum_forumuser', 'is_active')

        # Deleting field 'ForumUser.date_joined'
        db.delete_column(u'forum_forumuser', 'date_joined')

        # Removing M2M table for field groups on 'ForumUser'
        db.delete_table(db.shorten_name(u'forum_forumuser_groups'))

        # Removing M2M table for field user_permissions on 'ForumUser'
        db.delete_table(db.shorten_name(u'forum_forumuser_user_permissions'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forum.forum': {
            'Meta': {'object_name': 'Forum'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_forums'", 'to': u"orm['forum.ForumUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_forums'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['forum.Forum']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'forum.forumuser': {
            'Meta': {'object_name': 'ForumUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'forum.reply': {
            'Meta': {'object_name': 'Reply'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replies'", 'to': u"orm['forum.Thread']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forum.ForumUser']"})
        },
        u'forum.thread': {
            'Meta': {'object_name': 'Thread'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'op': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forum.ForumUser']"}),
            'parent_forum': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'threads'", 'to': u"orm['forum.Forum']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['forum']