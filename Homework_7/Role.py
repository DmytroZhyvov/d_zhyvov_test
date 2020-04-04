import requests


class Role:
    """Main Role class"""

    def __init__(self, url):
        """Constructor"""
        self.url = url  # base URL

    def create_role(self, role_name, role_type, role_level, book_url):
        """Create a role via REST"""

        url = self.url + 'roles'  # request URL

        data = {"name": role_name, "type": role_type, "level": role_level, "book": book_url}  # request body
        response = requests.post(url, data)  # send a post request

        return response  # REST response

    def update_role(self, role_name, role_type, role_level, book_url, role_id=None):
        """Update a role via REST"""

        url = self.url + 'roles/' + str(role_id)  # form an API endpoint
        data = {"name": role_name, "type": role_type, "level": role_level, "book": book_url}  # request body
        response = requests.put(url, data)  # send a put request

        return response  # REST response

    def delete_role(self, role_id=None):
        """Delete a role via REST by role id"""

        url = self.url + 'roles/' + str(role_id)  # form an API endpoint
        response = requests.delete(url)  # send a delete request

        return response

    def find_role_by_id(self, role_id=None):
        """Find a role via REST by role id"""

        url = self.url + 'roles/' + str(role_id)  # form an API endpoint
        response = requests.get(url)  # send a get request

        return response

    def get_all_roles(self):
        """Get all roles via REST"""

        url = self.url + 'roles'  # form an API endpoint
        response = requests.get(url)  # send a get request

        return response

    def get_role_from_book(self, book_id=None):
        """Get a role from a book by book id"""

        url = self.url + 'roles'

        payload = {'book_id': book_id}

        response = requests.get(url, params=payload)

        return response

    def get_role_by_type(self, type=None):
        """Get all roles by specified role type"""

        url = self.url + 'roles'

        payload = {'type': type}

        response = requests.get(url, params=payload)

        return response

    def get_role_by_level(self, level=None):
        """Get all roles by specified role level"""

        url = self.url + 'roles'

        payload = {'level': level}

        response = requests.get(url, params=payload)

        return response

    def get_role_by_level_param(self, level_lt=None, level_lte=None, level_gt=None, level_gte=None):
        """Get all roles by specified role level parameters"""

        url = self.url + 'roles'
        payload = None

        if level_lt:
            payload = {'level__lt': level_lt}  # get all roles, less than specified level

        if level_lte:
            payload = {'level__lte': level_lte}  # get all roles, less or equal to specified level

        if level_gt:
            payload = {'level__gt': level_gt}  # get all roles, greater than specified level

        if level_gte:
            payload = {'level__gte': level_gte}  # get all roles, greater or equal to specified level

        response = requests.get(url, params=payload)

        return response






