
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

########################################################################################################################

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

########################################################################################################################
#
# #ЭТО ВТОРОЙ ВАРИАНТ и НА МОЙ ВЗГЛЯД ПРАВИЛЬНЫЙ:
#
# from django.views.generic.edit import CreateView
# from .forms import BaseRegisterForm
# from sign.models import UserProfile
#
# ########################################################################################################################
#
# class BaseRegisterView(CreateView):
#     model = UserProfile
#     form_class = BaseRegisterForm
#     success_url = '/'
#
# ########################################################################################################################