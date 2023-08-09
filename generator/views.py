from django.shortcuts import render
import random
import string


# Create your views here
def generate_password(request, name):
    if name == 'easy':
        res = ''.join(random.choice(string.ascii_letters) for i in range(8, random.randint(5, 16)))
        return render(request, 'generator/password.html', {'res': res})

    elif name == 'medium':
        res = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8, random.randint(8, 19)))
        return render(request, 'generator/password.html', {'res': res})

    elif name == 'hard':
        res = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in
                      range(8, random.randint(9, 22)))
        return render(request, 'generator/password.html', {'res': res})
