from fasthtml.common import fast_app, serve
from pages.home import HomePage

app, rt = fast_app()


@rt("/")
def get():
    return HomePage(app, rt)


serve()
