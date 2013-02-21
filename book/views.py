# Create your views here.
from django.shortcuts import render_to_response
import datetime
def index(request):
     request.session['is_logged'] = datetime.datetime.now()
     return render_to_response("shop.html",dict(user=request.session['is_logged']))