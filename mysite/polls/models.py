from django.db import models


# models da aplicação
class Question(models.Model):
    # campos
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    # quando o obj é exibido reporta um campo
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
