from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_list(request):
    questions = Question.objects.all()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/question/list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    return render(request, 'qa/question/detail.html', {
        'question': question,
    })
