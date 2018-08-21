from django.shortcuts import render,redirect

def matches(requests):
    return render(requests,"matches.html",{})