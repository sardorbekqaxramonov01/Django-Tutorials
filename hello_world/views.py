from django.http import HttpResponse


def home(home):
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
        h1{
            color:blue;
        }
    </style>

    <h1>Hello world</h1>"""
)

def about(about):
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
        h1{
            color:blue;
        }
    </style>

    <h1>Salom dunyo</h1>"""
)
