from tabnanny import verbose
from django.db import models


# About Us Who Are We
class About (models.Model):
    who_are_we = models.TextField(max_length=100000, verbose_name="About Us")

    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "About us"

    def __str__(self):
        return "Change Or Add About Us"


# Our Services
class Our_Services (models.Model):
    img = models.ImageField(upload_to='services', verbose_name="Image")
    service_title = models.CharField(
        max_length=200, verbose_name="Title")
    service_description = models.TextField(
        max_length=150000, blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Our Service"
        verbose_name_plural = "Our Services"

    def __str__(self):
        return f"Change Or Add {self.service_title}"


# Image Our Services
class Img_services (models.Model):
    service_img = models.ImageField(upload_to='service_img', verbose_name="Image")
    service = models.ForeignKey(
        Our_Services, on_delete=models.CASCADE, verbose_name="Service", related_name="Service")

    # Metadata
    class Meta:
        verbose_name = "Image service"
        verbose_name_plural = "Image service"

    def __str__(self):
        return f"Change Or Add Image For {self.service.service_title}"


# Our Team
class Our_Team (models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Name")
    job = models.CharField(max_length=200, blank=True, null=True, verbose_name="Job")
    img = models.ImageField(upload_to='team_img', verbose_name="Image")
    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name="Phone Number")
    email = models.EmailField(max_length=200, blank=True, null=True, verbose_name="Email")
    facebook = models.URLField(max_length=200, blank=True, null=True, verbose_name="Facebook")
    twitter = models.URLField(max_length=200, blank=True, null=True, verbose_name="Twitter")


    class Meta:
        verbose_name = "Our Team"
        verbose_name_plural = "Our Team"

    def __str__(self):
        return self.name
