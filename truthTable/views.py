from operator import truediv
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise1, Exercise2
from .truth_table_generator import generate
from .truth_table_exercise1 import generate_exercise1
from .truth_table_exercise2 import generate_exercise2
from .truth_table_exercise2_validation import exercise2_validation
from .form import TruthTableForm

# Create your views here.

formula = ""
exercise1_id = 1
exercise2_id = 1
correct = 0
total = 0
hard = []
chosen = False
nxt = False


def generator_view(request):
    global formula, hard
    empty = False
    invalid = False
    if request.method == 'POST':
        if 'calculate' in request.POST:
            formula = request.POST.get('formula', None)
            if formula == '':
                empty = True
            else:
                try:
                    generate(formula)
                    return redirect("result/")
                except IOError:
                    invalid = True

        elif 'clean' in request.POST:
            hard = []

        else:
            for i in range(1, len(hard)+1):
                if str(i) in request.POST:
                    formula = hard[i-1]
                    return redirect("result/")
    
    context = {
        'nevbar': True,
        'empty': empty,
        'invalid': invalid,
        'hard': hard,
        'hard.length': len(hard)
    }

    return render(request, "truthTable/generator.html", context)

    # form = TruthTableForm(request.POST or None)
    #
    # if form.is_valid():
    #     formula = request.POST.get('formula', None)
    #     return redirect("result/")
    #
    # context = {
    #     'form': form
    # }
    # return render(request, "truthTable/generator.html", context)


def truth_table_view(request):
    global formula, hard
    truth_table = generate(formula)
    context = {
        'formula': formula,
        'truth_table': truth_table
    }
    return render(request, "truthTable/truth_table.html", context)


def exercise1_view(request):
    global exercise1_id, correct, total, nxt, chosen

    queryset = Exercise1.objects.all()

    if exercise1_id <= queryset.count():
        obj = queryset[exercise1_id-1]
        # print("id: ", queryset[exercise1_id-1].id)
    else:
        return redirect("../score")
    
    feedback = None
    answer = []
    # nxt = False
    # chosen = False

    value = generate_exercise1(obj.question)
    if generate_exercise1(obj.formula0) == value:
        answer.append('A')
    if generate_exercise1(obj.formula1) == value:
        answer.append('B')
    if generate_exercise1(obj.formula2) == value:
        answer.append('C')
    if not answer:
        answer.append('D')

    if request.method == 'POST':
        if 'A' in request.POST:
            chosen = True
            nxt = True
            if 'A' in answer:
                feedback = True
            else:
                feedback = False

        elif 'B' in request.POST:
            chosen = True
            nxt = True
            if 'B' in answer:
                feedback = True
            else:
                feedback = False

        elif 'C' in request.POST:
            chosen = True
            nxt = True
            if 'C' in answer:
                feedback = True
            else:
                feedback = False

        elif 'D' in request.POST:
            chosen = True
            nxt = True
            if 'D' in answer:
                feedback = True
            else:
                feedback = False

        elif 'hardA' in request.POST:
            if obj.question.replace(" ","") not in hard:
                hard.append(obj.question.replace(" ",""))
                print(hard)
                # print(type(obj.question))
        
        elif 'hardB' in request.POST:
            if obj.formula0.replace(" ","") not in hard:
                hard.append(obj.formula0.replace(" ",""))
                print(hard)
                # print(type(obj.formula0))

        elif 'hardC' in request.POST:
            if obj.formula1.replace(" ","") not in hard:
                hard.append(obj.formula1.replace(" ",""))
                print(hard)
                # print(type(obj.formula1))
        
        elif 'hardD' in request.POST:
            if obj.formula2.replace(" ","") not in hard:
                hard.append(obj.formula2.replace(" ",""))
                print(hard)
                # print(type(obj.formula2))
        

        if feedback is not None:
            total += 1

        if feedback is True:
            correct += 1

        # print(correct, " / ", total)

        if 'next' in request.POST:
            nxt = False
            chosen = False
            exercise1_id += 1
            return redirect("http://127.0.0.1:8000/truthTable/exercise1")

        if 'home' in request.POST:
            nxt = False
            chosen = False
            correct = 0
            total = 0
            exercise1_id = 1
            return redirect("http://127.0.0.1:8000/truthTable/")


    context = {
        'nevbar': False,
        'question': obj.question.replace(" ",""),
        'formula0': obj.formula0.replace(" ",""),
        'formula1': obj.formula1.replace(" ",""),
        'formula2': obj.formula2.replace(" ",""),
        'answer': answer,
        'feedback': feedback,
        'nxt': nxt,
        'chosen': chosen,
    }

    return render(request, "truthTable/exercise1.html", context)


def exercise2_view(request):
    global exercise2_id, correct, total, nxt, chosen

    queryset = Exercise2.objects.all()

    if exercise2_id <= queryset.count():
        obj = queryset[exercise2_id-1]
    else:
        return redirect("../score")

    exercise2 = generate_exercise2(obj.question, obj.values)
    feedback = None
    answer = exercise2[0]
    table = exercise2[1]
    # nxt = False
    # chosen = False

    if request.method == 'POST':
        if '1' in request.POST:
            chosen = True
            nxt = True
            if answer == 1:
                feedback = True
            else:
                feedback = False

        elif '0' in request.POST:
            chosen = True
            nxt = True
            if answer == 0:
                feedback = True
            else:
                feedback = False

        # print(correct, " / ", total)

        
        elif 'hard' in request.POST:
            if obj.question.replace(" ","") not in hard:
                hard.append(obj.question.replace(" ",""))
                print(hard)

        if 'next' in request.POST:
            nxt = False
            chosen = False
            exercise2_id += 1
            return redirect("http://127.0.0.1:8000/truthTable/exercise2")

        if 'home' in request.POST:
            nxt = False
            chosen = False
            correct = 0
            total = 0
            exercise2_id = 1
            return redirect("http://127.0.0.1:8000/truthTable/")



        if feedback is not None:
            total += 1

        if feedback is True:
            correct += 1

    context = {
        'nevbar': False,
        'question': obj.question.replace(" ",""),
        'feedback': feedback,
        'answer': answer,
        'table': table,
        'nxt': nxt,
        'chosen': chosen
    }
    return render(request, "truthTable/exercise2.html", context)


def score_view(request):
    global exercise1_id, exercise2_id, correct, total

    if request.method == 'POST':
        correct = 0
        total = 0
        exercise1_id = 1
        exercise2_id = 1
        return redirect("http://127.0.0.1:8000/truthTable/")

    context = {
        'nevbar': False,
        'correct': correct,
        'total': total
    }

    return render(request, "truthTable/score.html", context)


def exercise1_validation_view(request):
    queryset = Exercise1.objects.all()

    validation = []
    for obj in queryset:
        lst = [obj.id]
        try:
            generate(obj.question)
        except IOError:
            lst.append(-1)
        
        try:
            generate(obj.formula0)
        except IOError:
            lst.append(0)
        
        try:
            generate(obj.formula1)
        except IOError:
            lst.append(1)
        
        try:
            generate(obj.formula2)
        except IOError:
            lst.append(2)

        if len(lst) > 1:
            # print(lst)
            validation.append(lst)

    context = {
        'navbar': False,
        'list': validation
    }
    
    if validation == []:
        return exercise1_view(request)

    return render(request, "truthTable/exercise1_validation.html", context)

def exercise2_validation_view(request):
    queryset = Exercise2.objects.all()

    validation = []
    for obj in queryset:
        lst = [obj.id]
        try:    
            generate(obj.question)
        except IOError:
            lst.append(0)
        
        try:
            exercise2_validation(obj.question, obj.values)
        except IOError:
            lst.append(1)
        
        if len(lst) > 1:
            validation.append(lst)

    context = {
        'navbar': False,
        'list': validation
    }

    print(validation)
    
    if validation == []:
        return exercise2_view(request)

    return render(request, "truthTable/exercise2_validation.html", context)
