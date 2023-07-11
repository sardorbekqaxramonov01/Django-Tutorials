from django.http import HttpResponse


def home(request):
    return HttpResponse("""
    <style>
        *{
            padding:0;
            margin:0;
            box-sizing:border-box;
        }
        body{
            display:flex;
            justify-content:center;
            text-align:center;
        }
        a{
            color:blue;
            margin:10px;
        }
    </style>

    <a href="about/">about</a>
    <a href="project/">project</a>
    <a href="my_blog/">my_blog</a>
    <a href="contact/">contact</a>
    """
)

def about(request):
    return HttpResponse("""
    <style>
        *{
            padding:0;
            margin:0;
            box-sizing:border-box;
        }
        body{
            display:flex;
            justify-content:center;
            text-align:center;
        }
        a{
            color:blue;
        }
    </style>

    <a href="home/">home</a>
    <a href="project/">project</a>
    <a href="my_blog/">my_blog</a>
    <a href="contact/">contact</a>"""
)

def project(request):
    return HttpResponse("""
    <style>
        *{
            padding:0;
            margin:0;
            box-sizing:border-box;
        }
        body{
            display:flex;
            justify-content:center;
            text-align:center;
        }
        a{
            color:blue;
            margin:10px;
        }
    </style>
    <a href="home/">Home</a>
    <a href="about/">about</a>
    <a href="my_blog/">my_blog</a>
    <a href="contact/">contact</a>"""
)

def my_blog(request):
    return HttpResponse("""
    <style>
        *{
            padding:0;
            margin:0;
            box-sizing:border-box;
        }
        body{
            display:flex;
            justify-content:center;
            text-align:center;
        }
        a{
            color:blue;
            margin:10px;
        }
    </style>
                        
    <a href="home/">home</a>
    <a href="about/">about</a>
    <a href="project/">project</a>
    <a href="contact/">contact</a>"""
)

def contact(request):
    return HttpResponse("""
    <style>
        *{
            padding:0;
            margin:0;
            box-sizing:border-box;
        }
        body{
            display:flex;
            justify-content:center;
            text-align:center;
        }
        a{
            color:blue;
            margin:10px;
        }
    </style>

    <a href="home/">home</a>
    <a href="about/">about</a>
    <a href="my_blog/">my_blog</a>
    <a href="project/">project</a>"""
)