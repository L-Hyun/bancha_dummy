from django.db import models
from datetime import date

class ReviewManager(models.Manager):
  def create_review(self, linked_item, linked_user, score, text, written_date):
    review = self.model(
      linked_item = linked_item,
      linked_user = linked_user,
      score = score,
      text = text,
      written_date = written_date
    )

    review.save()
    return review

class Review(models.Model):
  review_id = models.AutoField(primary_key=True)
  linked_item = models.IntegerField(verbose_name="연결된 아이템")
  linked_user = models.CharField(max_length=255, verbose_name="작성자 닉네임")
  score = models.IntegerField(verbose_name="점수")
  text = models.TextField(verbose_name="본문")
  written_date = models.DateField(verbose_name="작성 일자", default=date.today)

  objects = ReviewManager()

  def __str__(self):
    return str(self.review_id)
  
  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True
