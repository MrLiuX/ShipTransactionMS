def jwt_response_payload_handler(token, user=None, request=None, role=None):
    return {
        'id': user.id,
        'username': user.username,
        'token': token,
    }