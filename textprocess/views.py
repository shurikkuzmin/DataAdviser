from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View, ListView, TemplateView
from django.shortcuts import render,render_to_response
from django.template import Context, loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.html import mark_safe
from django.core.urlresolvers import reverse

from models import QueryResult

import ast

import textMapSearch

def main_page(request):
    #return render(request, 'carousel.html')
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def replay_search(request,pkid):
    qr = get_object_or_404(QueryResult,pk=pkid)
    results = ast.literal_eval(qr.results)
    if results:
        results['the_featured_embed_'] = mark_safe(results.get('the_featured_embed_',""))
    city_name = textMapSearch.city_names.get(qr.search_city,textMapSearch.city_names['CGO']) # default is chicago
    return render(request, 'text_process.html', {'article_text': qr.submitted_text, 'search_city':city_name, 'keys': results, 'qr': qr})

def process_text(request):
    article_text = ""
    search_city = ""
    keys={}
    if request.method == 'POST':
        if "article_text" in request.POST:
            article_text = request.POST["article_text"]
            search_city = request.POST.get("search_city","CGO")
            keys = textMapSearch.find_keywords(article_text,search_city)
    
    qr = QueryResult(submitted_text=article_text,search_city=search_city,results=repr(keys),http_post_data=request.POST,metadata=repr(request.META))
    qr.save()
    
    
#    if "Artist tackles Chicago's pesky pothole problem" in article_text and "The perfect pothole might not exist for many people" in article_text and "No pun intended." in article_text:
#        return HttpResponseRedirect(reverse('replay_view',kwargs={'pkid': 9}))
    
#    if "The perfect pothole might not exist for many people" in article_text and "No pun intended." in article_text:
#        return HttpResponseRedirect(reverse('replay_view',kwargs={'pkid': 46}))
    
    return HttpResponseRedirect(reverse('replay_view',kwargs={'pkid': qr.id}))
    #return render_to_response('text_process.html', {'article_text': article_text, 'keys': keys})
	
def submit_to_email(request):
    important = ['articles_types','published_in','visualisation','features','data','email','comments']
    dict_important = {s: request.POST.get(s) for s in important}
    dict_important['raw'] = repr(request.POST)
    c = Context(dict_important)

    subject = '[Data Adviser] Submit to Email'
    from_email = 'no-reply@floatingpointlab.com'
    
    t_txt = loader.get_template('email_notification.txt')
    t_html = loader.get_template('email_notification.html')
    
    to_email = [a[1] for a in settings.ADMINS]

    text_content = t_txt.render(c)
    html_content = t_html.render(c)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    #TODO: set confirmation message
    return HttpResponseRedirect(reverse('main'))
    
