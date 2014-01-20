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
  name = models.CharField(max_length=200)
  release = models.ForeignKey(Release)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'tickets'


class Branch(models.Model):
  name = models.CharField(max_length=200)
  ticket = models.ForeignKey(Ticket)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'branches'
  

class Server(models.Model):
  name = models.CharField(max_length=200)
  ip = models.CharField(max_length=15)
  release = models.OneToOneField(Release)
  user = models.ForeignKey(User)
  def __unicode__(self):
    return self.name

  class Meta:
    db_table = 'servers'
