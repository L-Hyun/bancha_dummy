from django.db import models

class ItemManager(models.Manager):
  def create_item(self, title, category, seller, price, dPrice, tags, thu, det):
    if (not title):
      raise ValueError("must have title")
    if (not category):
      raise ValueError("must have category")
    if (not seller):
      raise ValueError("must have seller")
    
    item = self.model(
      title = title,
      categroy = category,
      seller = seller,
      price = price,
      discountedPrice = dPrice,
      hashtags = tags,
      thumb = thu,
      detail = det
    )

    item.save()
    return item

class Item(models.Model):
  item_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=50, verbose_name="아이템 제목")
  category = models.IntegerField(verbose_name="카테고리")
  seller = models.IntegerField(verbose_name="판매자 번호")
  price = models.IntegerField(verbose_name="가격", default=0)
  discountedPrice = models.IntegerField(verbose_name="할인가", default=0)
  hashtags = models.CharField(max_length=50, verbose_name="해쉬태그")
  thumb = models.ImageField(upload_to="items/thumb", blank=True)
  detail = models.ImageField(upload_to="items/detail", blank=True)

  objects = ItemManager()

  REQUIRED_FILED = ['title', 'category']

  def __str__(self):
    return self.title
  
  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True