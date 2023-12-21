from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    account = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        db_table = 'user'

class Panel(models.Model):
    pno = models.BigAutoField(primary_key=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'panel'

class Room(models.Model):
    rno = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'room'

class Sensor(models.Model):
    sno = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    data = models.IntegerField()
    panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='panel_pno', blank=True, null=True)

    class Meta:
        db_table = 'sensor'

class Rule(models.Model):
    rno = models.BigAutoField(primary_key=True)
    scene = models.CharField(max_length=45, blank=True, null=True)
    panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='panel_pno', blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_uid', blank=True, null=True)

    class Meta:
        db_table = 'rule'

# class Shiyong(models.Model):
#     uno = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_uid', blank=True, null=True)
#     panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='panel_pno', blank=True, null=True)

#     class Meta:
#         db_table = 'shiyong'

class Furniture(models.Model):
    fno = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_rno', blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='panel_pno', blank=True, null=True)

    class Meta:
        db_table = 'furniture'

class Control(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, db_column='rule_rno')
    panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='panel_pno', blank=True, null=True)
    sensor = models.ForeignKey(Sensor, models.DO_NOTHING, db_column='sensor_sno', blank=True, null=True)
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_rno', blank=True, null=True)
    furniture = models.ForeignKey(Furniture, models.DO_NOTHING, db_column='furniture_fno', blank=True, null=True)

    class Meta:
        db_table = 'control'