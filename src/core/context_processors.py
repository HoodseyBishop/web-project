from webProject import cache
from questions.models import Question


def overall_stats(request):
    total_questions = cache.get('total_questions')
    if total_questions is None:
        total_questions = Question.objects.count()
        cache.set('total_questions', total_questions, 15)
    result = {'total_questions': total_questions}
    return result