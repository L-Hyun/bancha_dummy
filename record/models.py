from django.db import models
from datetime import datetime

class RecordManager(models.Manager):
  def create_review(self, ordered_date, experience_date, linked_item, linked_user, orderer_name, orderer_phone, orderer_email):
    record = self.model(
      ordered_date = ordered_date,
      experience_date = experience_date,
      linked_item = linked_item,
      linked_user = linked_user,
      orderer_name = orderer_name,
      orderer_phone = orderer_phone,
      orderer_email = orderer_email
    )

    record.save()
    return record

class Record(models.Model):
  record_id = models.AutoField(primary_key=True)
  ordered_date = models.DateTimeField(verbose_name="주문 일자", default=datetime.now)
  experience_date = models.DateField(verbose_name="체험 일자")
  linked_item = models.IntegerField(verbose_name="연결된 아이템")
  linked_user = models.CharField(max_length=255, verbose_name="주문자 닉네임")
  orderer_name = models.CharField(max_length=255, verbose_name="주문에 쓰인 이름")
  orderer_phone = models.CharField(max_length=255, verbose_name="주문에 쓰인 전화번호")
  orderer_email = models.CharField(max_length=255, verbose_name="주문에 쓰인 이메일")

  objects = RecordManager()

  def __str__(self):
    return str(self.record_id)
  
  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True
