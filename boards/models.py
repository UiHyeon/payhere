from django.db import models
from accounts.models import User

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")
    memo = models.CharField("메모", max_length=100, null=False)
    price = models.IntegerField("금액", null=False)
    dt_created = models.DateTimeField("작성일", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField("수정일", auto_now=True, null=False)

    def __str__(self):
        return self.title
