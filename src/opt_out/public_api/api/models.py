from django.db import models


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    self_submission = models.BooleanField(default=True)

    identity = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    interaction = models.CharField(max_length=200)


class URL(models.Model):
    id = models.AutoField(primary_key=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, default=1)
    url = models.CharField(max_length=200)
