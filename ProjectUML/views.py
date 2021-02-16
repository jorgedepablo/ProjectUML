from django.http import HttpResponse

def home(request):

    template="""
    <html> 
    <h1>
    WELCOME TO UML PROJECT 
    </h1> 
    </html>"""

    return HttpResponse(template)