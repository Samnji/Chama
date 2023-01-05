from django.shortcuts import render
from django.views.generic import ListView
from .models import Member

class MemberListView(ListView):
    model = Member
    template_name='member_list.html'
