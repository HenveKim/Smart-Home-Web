from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.BigAutoField(primary_key=True,verbose_name="uid号")
    username = models.CharField(max_length=10, blank=True, null=True,verbose_name="用户名")
    password = models.CharField(max_length=45, blank=True, null=True,verbose_name="密码")
    email = models.CharField(max_length=20, blank=True, null=True,verbose_name="邮箱")
    phonenumber = models.CharField(max_length=20, blank=True, null=True,verbose_name="手机号")
    class Meta:
        db_table = 'user'

class Room(models.Model):
    rno = models.BigAutoField(primary_key=True,verbose_name="rno号")
    name = models.CharField(max_length=45,verbose_name="房间名")
    num = models.IntegerField(verbose_name="家具数",default=0)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'room'

class Furniture(models.Model):
    state_choices = (
        (0, "关"),
        (1, "开"),
    )
    fno = models.BigAutoField(primary_key=True,verbose_name="fno号")
    state = models.SmallIntegerField(verbose_name="状态", choices=state_choices, default=0)
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_rno', blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True,verbose_name="家具名")

    class Meta:
        db_table = 'furniture'

class Panel(models.Model):
    state_choices = (
        (0, "关"),
        (1, "开"),
    )
    pno = models.BigAutoField(primary_key=True,verbose_name="pno号")
    start_time = models.DateTimeField(blank=True, null=True,verbose_name="开始时间")
    end_time = models.DateTimeField(blank=True, null=True,verbose_name="结束时间")
    fno = models.IntegerField(verbose_name="编号",db_column='fno',blank=False, null=False,default=None)
    state = models.SmallIntegerField(verbose_name="状态",blank=False, null=False,default=None,choices=state_choices)
    def __str__(self):
        return self.fno
    class Meta:
        db_table = 'panel'

class Sensor(models.Model):
    sno = models.BigAutoField(primary_key=True,verbose_name="sno号")
    name = models.CharField(max_length=45,verbose_name="传感器名")
    data = models.IntegerField(verbose_name="数据")
    panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='panel_pno', blank=True, null=True)

    class Meta:
        db_table = 'sensor'

class Rule(models.Model):
    rno = models.BigAutoField(primary_key=True,verbose_name="rno号")
    scene = models.CharField(max_length=45, blank=True, null=True,verbose_name="场景")
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



class Control(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, db_column='rule_rno',verbose_name="规则")
    panel = models.ForeignKey(Panel, models.DO_NOTHING, db_column='panel_pno', blank=True, null=True)
    sensor = models.ForeignKey(Sensor, models.DO_NOTHING, db_column='sensor_sno', blank=True, null=True)
    room = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_rno', blank=True, null=True)
    furniture = models.ForeignKey(Furniture, models.DO_NOTHING, db_column='furniture_fno', blank=True, null=True)

    class Meta:
        db_table = 'control'

