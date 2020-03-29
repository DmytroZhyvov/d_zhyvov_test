import requests


def manage_book(action=None, title=None, author=None, book_id=None):
    """Main function for various operations with book"""

    url = 'http://pulse-rest-testing.herokuapp.com/'  # set a main URL

    # request body
    data = {
                "title": title,
                "author": author
            }

    response = None

    if action == 'create' and title is not None and author is not None:  # create a book and check mandatory attributes
        url = url + 'books'  # form an API endpoint
        response = requests.post(url, data)  # send a post request with a payload

    if action == 'update' and book_id is not None:  # update a book and check mandatory attribute
        url = url + 'books/' + str(book_id)  # form an API endpoint
        response = requests.put(url, data)  # send a put request with a payload

    if action == 'delete' and book_id is not None:  # delete a book and check mandatory attribute
        url = url + 'books/' + str(book_id)  # form an API endpoint
        response = requests.delete(url)  # send a delete request

    if action == 'get_books':  # get all books
        url = url + 'books'  # form an API endpoint
        response = requests.get(url)  # send a get request

    if action == 'find_book' and book_id is not None:  # get a book by book Id
        url = url + 'books/' + str(book_id)  # form an API endpoint
        response = requests.get(url)  # send a get request

    return response  # get a response object


def manage_role(action=None, role_name=None, role_type=None, role_level=None, book=None, role_id=None):
    """Main function for various operations with role"""

    url = 'http://pulse-rest-testing.herokuapp.com'  # set a main URL

    response = None

    # request body
    data = {
                "name": role_name,
                "type": role_type,
                "level": role_level,
                "book": book
            }
    #  create a role and check mandatory attributes
    if action == 'create' and role_name is not None and role_type is not None and role_level and book is not None:
        url = url + '/roles'  # form an API endpoint
        response = requests.post(url, data)  # send a post request with a payload

    if action == 'update' and role_id is not None:  # update a role and check mandatory attribute
        url = url + '/roles/' + str(role_id)  # form an API endpoint
        response = requests.put(url, data)  # send a put request with a payload

    if action == 'delete' and role_id is not None:  # delete a role
        url = url + '/roles/' + str(role_id)  # form an API endpoint
        response = requests.delete(url)  # send a delete request

    if action == 'get_roles':  # get all roles
        url = url + '/roles'  # form an API endpoint
        response = requests.get(url)

    if action == 'find_role' and role_id is not None:  # get a role by role Id
        url = url + '/roles/' + str(role_id)  # form an API endpoint
        response = requests.get(url)  # send a get request

    return response  # get a response object

#
# handle_book(action='delete', id=240)

