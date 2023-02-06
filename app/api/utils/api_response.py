
class ApiResponse:
    def __init__(self, message, success, status, data):
        self.message = message
        self.success = success
        self.status = status
        self.data = data

    def __init__(self, message, success, status):
        self.message = message
        self.success = success
        self.status = status

    def __init__(self, message, success):
        self.message = message
        self.success = success
