from django.db import models
from django.urls import reverse

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    question_votes = models.IntegerField(default=0)
    question_author = models.CharField(max_length=20, default="Anonymous")
    tags = models.ManyToManyField("Tag", blank=True, related_name="tags")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question.question_text}?; choice - {self.choice_text}"

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    tag_text = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.tag_text
    
    def get_absolute_url(self):
        return reverse("polls:tag_search", kwargs={"tag":self.tag_text})
    
