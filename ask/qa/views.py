from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from qa.models import Question
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator


def question_list(request):
    qs = Question.objects.all()
    qs = qs.order_by('-added_at')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('question_list') + '?page='

    return render(request, 'list.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def popular(request):
    qs = Question.objects.all()
    qs = qs.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'list_rating.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'detail.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })


def question_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            ask = form.save()
            url = reverse('question_detail', args=[ask.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'ask.html', {
        'form': form
    })


def question_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            url = reverse('question_detail', args=[answer.question.id])
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
