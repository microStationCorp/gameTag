from django.shortcuts import render
from . import utils
from random import randint
# Create your views here.


def home(response):
    if response.method == 'POST':
        prefix = response.POST['pre']
        suffix = response.POST['suf']
        name_list = utils.get_data()
        random_name = name_list[randint(0, 5902)]
        genName = "Generated Name : "+prefix+random_name+suffix
        return render(response, 'home/home.html', {'gen': genName})
    else:
        return render(response, 'home/home.html')
