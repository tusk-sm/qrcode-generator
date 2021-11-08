from views import  handle

def setup_routes(app):
    router = app.router
    router.add_get('/', handle, name='base')
    

   