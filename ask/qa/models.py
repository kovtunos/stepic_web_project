from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True)
    author = models.ForeignKey(User)
    likes = models.TextField(blank=True)

    class Meta:
        ordering = ('-added_at',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answers')
    author = models.ForeignKey(User)

    class Meta:
        ordering = ('added_at',)

    def __unicode__(self):
        return 'Answer by {}'.format(self.author)


# TODO: when upgrading don't forget to rename __unicode__ to __str__
