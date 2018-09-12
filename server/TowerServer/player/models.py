import binascii
import os

from django.db import models


class UserToken(models.Model):
    """
    The custom authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(
        'Player', related_name='auth_token',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(UserToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()


class Player(models.Model):
    username = models.CharField(max_length=32, null=False, verbose_name="账号")
    password = models.CharField(max_length=32, null=False, verbose_name="密码")
    email = models.EmailField(null=False, verbose_name="电子邮箱")

    nickname = models.CharField(max_length=16, null=False, verbose_name="昵称")
    hp = models.PositiveIntegerField(null=False, default=0, verbose_name="生命值")
    atk = models.PositiveIntegerField(null=False, default=0, verbose_name="攻击力")
    defense = models.PositiveIntegerField(null=False, default=0, verbose_name="防御力")
    coin = models.PositiveIntegerField(null=False, default=0, verbose_name="金币")

    post_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "玩家"
        verbose_name_plural = verbose_name
