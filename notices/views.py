# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def notices_list(request):
    return render(request, 'notices/notices_list.html', {})
# Create your views here.
