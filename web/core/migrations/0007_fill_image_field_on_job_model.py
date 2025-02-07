# Generated by Django 3.0 on 2019-12-29 18:24

from django.db import migrations

from lib.twitter import Twitter


def collect_image_urls(apps, _schema_editor):
    for job in apps.get_model("core", "Job").objects.filter(image=""):
        job.image = Twitter(job.screen_name).image
        job.save()


class Migration(migrations.Migration):
    dependencies = [("core", "0006_add_image_field_to_job_model")]
    operations = [migrations.RunPython(collect_image_urls)]
