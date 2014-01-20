from django.db import models

class User(models.Model):
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'users'


class Release(models.Model):
  name = models.CharField(max_length=200)
  user = models.ForeignKey(User)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'releases'


class Ticket(models.Model):
  release = models.ForeignKey(Release)
  name = models.CharField(max_length=200)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'tickets'


class Branch(models.Model):
  ticket = models.ForeignKey(Ticket)
  name = models.CharField(max_length=200)
  release = models.ForeignKey(Release)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'branches'
  

class Server(models.Model):
  name = models.CharField(max_length=200)
  user = models.ForeignKey(User)
  ip = models.CharField(max_length=15)
  release = models.OneToOneField(Release)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'servers'
