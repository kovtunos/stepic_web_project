from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_list(request):
    # TODO: use class-based views
    questions = Question.objects.all()
    questions = Question.objects.order_by('-added_at')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    # TODO: remove hardcode
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/question/list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def popular(request):
    # TODO: use class-based views
    questions = Question.objects.all()
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    # TODO: remove hardcode
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'qa/question/list_rating.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    return render(request, 'qa/question/detail.html', {
        'question': question,
        'answers': answers,
    })
