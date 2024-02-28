from .models import CustomUser
# In your app's context_processors.py
def session_data(request):
    return {'session': request.session}



def username_data(request):
    username = request.session.get('username')
    # print("Username:", username)  # Add this line for debugging
    if username:
        return {'username': username}
    else:
        return {}
