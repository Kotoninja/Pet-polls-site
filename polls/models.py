from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=50)
    question_votes = models.IntegerField(default=0)
    question_author = models.CharField(max_length=20, default="Anonymous")
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return f"user - {self.question_author}; question - {self.question_text}; count of votes - {self.question_votes}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question.question_text}?; choice - {self.choice_text}; votes - {self.choice_votes}"

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    tag_text = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.tag_text
