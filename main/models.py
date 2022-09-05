from django.db import models


# Start Settings Website
class Settings(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True,
                             null=True, verbose_name="Logo")
    phone = models.CharField(max_length=200, blank=True,
                             null=True, verbose_name="Phone")
    email = models.EmailField(
        max_length=200, blank=True, null=True, verbose_name="Email")
    address = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Address")
    facebook = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Facebook")
    twitter = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Twitter")
    instagram = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Instagram")
    youtube = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Youtube")
    whatsapp = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Whatsapp")
    telegram = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Telegram")

    def __str__(self):
        return 'Add Or Change Settings'


# Start Message
class Message (models.Model):
    name = models.CharField(max_length=200, blank=True,
                            null=True, verbose_name="Name")
    email = models.EmailField(max_length=200, verbose_name="Email")
    subject = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Subject")
    message = models.TextField(max_length=200,  verbose_name="Message")
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = "Message"

    def __str__(self):
        return f" Some One Ask us Name:{self.name}"
