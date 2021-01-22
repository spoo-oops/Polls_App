from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
#from django.views import generic
from .models import Choice, Question, Category
from django.utils import timezone

# This code loads template called poll/index/html and passes it a context. The context in a dictionary mapping template variable names to Python objects
def category(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
        }
    return render(request, 'polls/category.html', context)

def index(request, category_id):
    #template_name = 'polls/index.html'
    cat_question = Question.objects.filter(category=category_id)
    context = {
        'cat_question': cat_question,
        'category_id': category_id,
        }
    return render(request, 'polls/index.html', context)
    


def detail(request, category_id, question_id):
    #model = Question
    #emplate_name = 'polls/detail.html'
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question': question,
        'category_id': category_id,
        }
    return render(request, 'polls/detail.html', context)

    """def get_queryset(self):
        
        Excludes any questions that aren't published yet.
        
        return Question.objects.filter(pub_date__lte=timezone.now())"""


"""class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'"""
def results(request, category_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
        'category_id': category_id,
        }
    return render(request, 'polls/results.html', context)


def vote(request, category_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'category_id': category_id,
            'question': question,
            'error_message': "You didn't select a choice!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(category_id, question.id,)))

"""class ExtraView(generic.DetailView):
    model = Result
    template_name = 'polls/extra.html'

    def get_queryset(self):
        
        Return the last five published questions (not including those set to be
        published in the future).
        
        return Result.objects.filter(
            pub_date__lte=timezone.now()
        )
        """