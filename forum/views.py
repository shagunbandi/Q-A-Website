from django.views import generic
from .models import Question, Answer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.views.generic import View
from .forms import UserForm, UpdateProfile
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):

    template_name = 'forum/index.html'
    context_object_name = 'all_ques'

    def redirect(self):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/forum/')

    def get_queryset(self):
        return Question.objects.all()


class ReadView(generic.ListView):
    template_name = 'forum/read.html'
    context_object_name = 'all_ques'

    def get_queryset(self):
        return Question.objects.all()


class MyView(generic.ListView):
    template_name = 'forum/myquestions.html'
    context_object_name = 'all_ques'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'forum/details.html'


class QuestionCreate(CreateView):
    model = Question
    fields = ['ques']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.ques_author = self.request.user.username
        object.ques_date = datetime.now()
        object.save()
        return super(QuestionCreate, self).form_valid(form)


class QuestionUpdate(UpdateView):
    model = Question
    fields = ['ques', 'ques_author', 'ques_date']


class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('forum:index')


class AnswerCreate(CreateView):
    model = Answer
    fields = ['ans']

    def form_valid(self, form):
        object = form.save(commit=False)
        pkey = int(self.kwargs['pk'])
        ques = Question.objects.get(pk=pkey)
        object.question = ques
        object.ans_author = self.request.user.username
        object.ans_date = datetime.now()
        object.save()
        return super(AnswerCreate, self).form_valid(form)


class AnswerUpdate(UpdateView):
    model = Answer
    fields = ['ans']


class AnswerDelete(DeleteView):
    model = Answer
    success_url = reverse_lazy('forum:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'forum/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember_me']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    if not remember:
                        request.session.set_expiry(0)
                    return redirect('forum:index')
                    # to print out details --- request.user.username

        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/forum/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            remember = request.POST.get('remember_me')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if not remember:
                        request.session.set_expiry(0)
                    all_ques = Question.objects.all()
                    return render(request, 'forum/index.html', {'all_ques': all_ques})
                else:
                    return render(request, 'forum/login.html')
            else:
                return render(request, 'forum/login.html')
        return render(request, 'forum/login.html')


def update_profile(request):
    args = {}

    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        form = UpdateProfile(request.POST, instance=request.user)
        form.actual_user = request.user
        required_keyword = 'Bandi'
        if form.is_valid() and keyword == required_keyword:
            form.save()
            return HttpResponseRedirect('/forum/')
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'forum/registration_form.html', args)

