class User:
    """
    class that generates new instances of user
    """

    user_list = []

    def __init__(self,first_name,middle_name,password):
        self.first_name = first_name
        self.middle_name = middle_name
        self.password = password

    def save_user(self):
        """
        save_user method saves a new user objects to the user_list
        """

        User.user_list.append(self)
