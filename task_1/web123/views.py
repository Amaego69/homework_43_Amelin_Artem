from django.shortcuts import render


# Create your views here.


def index_view(request):
    if request.method == 'POST':
        print(request.POST)
    else:
        return render(request, 'index.html', context={'var_1': 'John'})


def calculator_view(request):
    error_messages = {
        'first_number': '',
        'second_number': '',
        'total': '',
    }

    if request.method == 'GET':
        return render(request, 'calculator.html', error_messages)
    elif request.method == 'POST':
        data = request.POST
        context = {
            'first_number': data.get('first_number'),
            'second_number': data.get('second_number'),
            'operation': data.get('operation'),
            'result': ''
        }

        if len(context) == 4:
            if context['operation'] is not None:
                try:
                    float(context['first_number'])
                    try:
                        float(context['second_number'])
                        if context['second_number'] == '0' and context['operation'] == '/':
                            error_messages['second_number'] = 'О нет, вы делите на 0. Бегите, вселенная схлопывается.'
                            return render(request, 'calculator.html', error_messages)
                        else:
                            match context['operation']:
                                case '+':
                                    context['result'] = str(float(context['first_number']) +
                                                            float(context['second_number'])).rstrip('0').rstrip('.')
                                    return render(request, 'answer.html', context)
                                case '-':
                                    context['result'] = str(float(context['first_number']) -
                                                            float(context['second_number'])).rstrip('0').rstrip('.')
                                    return render(request, 'answer.html', context)
                                case '*':
                                    context['result'] = str(float(context['first_number']) *
                                                            float(context['second_number'])).rstrip('0').rstrip('.')
                                    return render(request, 'answer.html', context)
                                case '/':
                                    context['result'] = str(float(context['first_number']) /
                                                            float(context['second_number'])).rstrip('0').rstrip('.')
                                    return render(request, 'answer.html', context)

                    except ValueError:
                        error_messages['second_number'] = 'Введите корректное число!'
                        return render(request, 'calculator.html', error_messages)
                except ValueError:
                    error_messages['first_number'] = 'Введите корректное число!'
                    return render(request, 'calculator.html', error_messages)
            else:
                error_messages['total'] = 'Все поля должны быть заполнены!'
                return render(request, 'calculator.html', error_messages)


