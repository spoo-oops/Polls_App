import datetime
from django.db import models
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length = 50, default='SOME STRING')
    category_desc = models.CharField(max_length = 500, default='SOME STRING')
    category_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.category_name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Important to add this method when dealing w/ interactive promopt
    def __str__(self):
        return self.question_text
    # Add custom date/time method

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
  # Relationship defined w/ Foreign Key
  # FK tells Django each key related to single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

"""class Result(models.Model):
    result_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Important to add this method when dealing w/ interactive promopt
    def __str__(self):
        return self.result_text
    # Add custom date/time method"""