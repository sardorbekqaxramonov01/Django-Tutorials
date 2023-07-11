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

    <a href="/about">About</a>
    <a href="/project">Project</a>
    <a href="/my_blog">My_blog</a>
    <a href="/contact">Contact</a>
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

    <a href="/home">Home</a>
    <a href="/project">Project</a>
    <a href="/my_blog">My_blog</a>
    <a href="/contact">Contact</a>"""
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
    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="/my_blog">My_blog</a>
    <a href="/contact">Contact</a>"""
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
                        
    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="/project">Project</a>
    <a href="/contact">Contact</a>"""
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

    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="/my_blog">My_blog</a>
    <a href="/project">Project</a>"""
)