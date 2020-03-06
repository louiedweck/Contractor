from django.db import models
from django.conf import settings

# Create your models here.


class Meta:
    verbose_name_plural = "pages"


class Page(models.Model):

    team_name = models.CharField(max_length=100)
    help_text = "Write the name fo the team you're betting on"

    author = models.CharField(max_length=100)

    wager = models.TextField()

    instructions = models.TextField(
        help_text="Write the instructions of your recipe")

    description = models.TextField(
        help_text="Write the desciption of your recipe")

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wager


class Comment(models.Model):

    page = models.ForeignKey(Page, on_delete=models.CASCADE)
