# roj/management/commands/import_jobs.py
from django.core.management.base import BaseCommand
from scrap.scrap import fetch_jobs
from roj.models import Job 

class Command(BaseCommand):
    help = "Import jobs from RemoteOK"

    def handle(self, *args, **kwargs):
        jobs = fetch_jobs()
        for job in jobs:
            Job.objects.update_or_create(
                external_id=job["external_id"],
                defaults={
                    "title": job["title"],
                    "company": job["company"],
                    "tags": job["tags"],
                    "url": job["url"],
                }
            )
        self.stdout.write(self.style.SUCCESS(f"✅ Imported {len(jobs)} jobs successfully!"))
