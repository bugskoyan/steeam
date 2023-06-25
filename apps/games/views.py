from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    html_code : str = "<h1>Hello Nibba</h1>"
    response: HttpResponse = HttpResponse(html_code)
    return response


def random(request: HttpRequest) -> HttpResponse:
    html_code_rndm : str = """
            <!DOCTYPE html>
        <html>
        <head>
            
            <script>
                function generateRandomNumber() {
                    var randomNumber = Math.floor(Math.random() * 101);
                    document.getElementById("randomNumberDisplay").innerHTML = randomNumber; 
                }
            </script>
        </head>
        <body>
            <h1>Случайное число: <span id="randomNumberDisplay"></span></h1>
            <button onclick="generateRandomNumber()">Генерировать число</button>
        </body>
        </html>

    """
    response: HttpResponse = HttpResponse(html_code_rndm)
    return response


def about(request: HttpRequest) -> HttpResponse:
    html_code_about : str = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                li {
                    border: 1px solid black;
                    padding: 10px;
                    margin-bottom: 10px;
                }
                h2 {
                    margin-top: 0;
                }
            </style>
        </head>
        <body>
            
            <ul>
                <li>
                    <img src="https://upload.wikimedia.org/wikipedia/ru/a/a2/The_Witcher_3-_Wild_Hunt_Cover.jpg" alt="">
                    <p>«Ведьма́к 3: Дикая Охота» — компьютерная игра в жанре action/RPG, разработанная польской студией CD Projekt RED.</p>
                </li>
                <li>
                    <img src="https://cdn.akamai.steamstatic.com/steam/apps/489830/header.jpg?t=1650909796" alt="">
                    <p>The Elder Scrolls V: Skyrim — компьютерная игра в жанре action/RPG с открытым миром, разработанная студией Bethesda Game Studios и выпущенная компанией Bethesda Softworks. </p>
                </li>
                <li>
                    <img src="https://cdn.akamai.steamstatic.com/steam/apps/22380/capsule_616x353.jpg?t=1665072891" alt="">
                    <p>Fallout: New Vegas — компьютерная ролевая игра с открытым миром, разработанная американской компанией Obsidian Entertainment и выпущенная Bethesda Softworks в 2010 году для Microsoft Windows, PlayStation 3 и Xbox 360. В России игра была выпущена компанией 1С. </p>
                </li>
                
            </ul>
        </body>
        </html>

    """
    response: HttpResponse = HttpResponse(html_code_about)
    return response


def round(request:HttpRequest)->HttpResponse:
    return HttpResponse(
        """<!DOCTYPE html>
            <html>
            <head>
            <style>
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            .spinner {
                margin: auto;
                width: 50px;
                height: 50px;
                border: 5px solid #f3f3f3;
                border-top: 5px solid #3498db;
                border-radius: 50%;
                animation: spin 2s linear infinite;
            }
            </style>
            </head>
            <body>
                <div class="spinner"></div>
            </body>
            </html>
            """
    )


def test_render(request: HttpRequest) -> HttpResponse:
    template_name :str = 'games/index.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

def main_page(request: HttpRequest) -> HttpResponse:
    page_main : str = 'games/mainpage.html'
    return render(
        request=request,
        template_name=page_main,
        context={}
    )