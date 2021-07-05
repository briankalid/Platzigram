from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#posts views
# Create your views here.

from datetime import datetime

from django.http import HttpResponse

posts=[
        {
            'name':'Mont Blac',
            'user':'Jessica Cortes',
            'timestamp': datetime.now(),
            'picture' : 'https://picsum.photos/200/200/?image=1036'
            },
        {
            'name':'Via lactea',
            'user':'C. Vander',
            'timestamp':datetime.now(),
            'picture':'https://picsum.photos/200/200/?image=903'
            },
        {
            'name':'Nuevo auditorio',
            'user':'Thespianartist',
            'timestamp':datetime.now(),
            'picture':'https://picsum.photos/200/200/?image=1076'
            }
        ]


posts_html=[
        {
            'title':'Mont Blac',
            'user':{
                'name':'Jessica Cortes',
                'picture':'https://picsum.photos/60/60/?image=1027'
                },
            'timestamp': datetime.now(),
            'photo' : 'https://picsum.photos/500/500/?image=1036'
            },
        {
            'name':'Via lactea',
            'user':{
                'name':'C. Van Der',
                'picture':'https://picsum.photos/60/60/?image=1005'
                },
            'timestamp':datetime.now(),
            'photo':'https://picsum.photos/500/500/?image=903'
            },
        {
            'name':'Nuevo auditorio',
            'user': {
                'name':'hespianartist',
                'picture':'https://picsum.photos/60/60/?image=803'
                },
            'timestamp':datetime.now(),
            'photo':'https://picsum.photos/500/500/?image=1076'
            }
        ]


def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>""".format(**post))
    return HttpResponse('<br>'.join(content))

@login_required
def list_posts_html(request):
    return render(request,'posts/feed.html',{'posts':posts_html})
