from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.http.request import HttpRequest
from django.urls import reverse
from django.shortcuts import redirect
from .models import FAQ
from .telegram import send_answer

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'is_sent',)
    change_form_template = 'admin/faq_change_form.html'
    
    fieldsets = (
        (None, {'fields': ('question', 'user', 'answer', 'is_sent',)}),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.is_sent is False:
            return ('question', 'user', 'is_sent',)
        return ('question', 'user', 'is_sent', 'answer',)

    def has_add_permission(self, request, obj=None):
        return False

    def response_change(self, request, obj):
        if request.method == 'POST':
            
            if '_send-answer' in request.POST:
                if obj.answer == '' or obj.answer == None:
                    self.message_user(request, 'Please write an answer before sending!', level=messages.ERROR)
                    return redirect(".") 
                message_request = send_answer(obj.user.chat_id, obj.question, obj.answer)
                
            if '_decline-question' in request.POST:
                decline_message = 'Наразі неможливо дати відповідь на ваше запитання.'
                message_request = send_answer(obj.user.chat_id, obj.question, decline_message)
            
            if message_request == 200:
                obj.is_sent = True
                if '_decline-question' in request.POST:
                    obj.answer = decline_message
                obj.save()
                self.message_user(request, 'Message successfully sended!')
            else:
                self.message_user(request, 'Message not sent, try again or later.', level=messages.ERROR)
                
            return redirect(reverse('admin:%s_%s_changelist' % (obj._meta.app_label,  obj._meta.model_name)))
        
        return super().response_change(request, obj)