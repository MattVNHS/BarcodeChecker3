from django.shortcuts import render

def home_screen_view(request):
    # How to create a variable
    # returns variables from this view file and allows us to put it into html (or elsewhere),
    # need to create a context variable as this is what we are passing to that html

    # Below is are 3 examples of creating variables
    # Example 1
    # context = {}
    # context['some_string'] = 'this is some string being passed onto the view'
    # context['some_number'] = 12345

    # Example 2
    # context = {
    #     'some_sting': 'this is some string being passed onto the view',
    #     'some_number': 12345,
    # }

    # Example 3 - this also makes a list of variables
    # context = {}
    # list_of_values = ["first entry", "second entry", "third entry", "fourth entry"]
    # context['list_of_values'] = list_of_values
    # Note: The name is context[] does not need to match the variable above.

    # Example 4 - this is another way of making a list of variables
    context = {}
    list_of_values = []
    list_of_values.append('first value')
    list_of_values.append('second value')
    list_of_values.append('third value')
    list_of_values.append('fourth value')
    context['list_of_values'] = list_of_values
    return render(request, 'personal/home.html', context)
