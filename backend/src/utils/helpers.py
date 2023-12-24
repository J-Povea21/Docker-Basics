def user_added_response(userCreated):
    message = 'User added!' if userCreated else 'The username is already taken'
    return {'status': userCreated, 'message': message}

def check_username_response(db_user):
    message = 'Username available!' if not db_user else 'Username not available'
    return {'status': not db_user, 'message': message}