import markdown
from django.db import models

# Create your models here.
from donator.models import User

default_markdown_file = 'static/data/default_markdown.txt'
default_markdown = ''

with open(default_markdown_file, 'r') as f:
    for line in f:
        default_markdown += line + "\n"


class Org(models.Model):
    description = models.TextField(max_length=5000, blank=True, default=default_markdown)
    name = models.CharField(max_length=30, null=True, blank=True)

    def markdownify(self):
        return markdown.markdown(self.description, safe_mode='escape')

    def ownername(self):
        userQS = User.objects.filter(org=self)

        if len(userQS) is 0:
            return None

        user = userQS[0]  # get user from queryset
        return user.username
