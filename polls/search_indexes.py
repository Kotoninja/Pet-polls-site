from haystack import indexes
from .models import Question


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr = "question_text")
    author = indexes.CharField(model_attr = "question_author")
    
    def get_model(self):
        return Question

    def index_queryset(self, using=None):
        return self.get_model().objects.all()