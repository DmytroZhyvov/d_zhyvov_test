import requests  # import HTTP library
import pytest   # import library for tests running
import json  # import JSON library
from Homework_8.vars import *  # import variables, used in tests and fixtures


@pytest.fixture
def basic_http_auth():
    """Construct auth parameter for HTTP Basic Auth"""

    auth = (username, password)
    return auth


@pytest.fixture(scope="session", autouse=True)
def header_w_user_auth_token():
    """Get headers with auth token using user's credentials"""

    data = {"username": username, "password": password}  # use username and password variables
    headers = {'Authorization': f'Token {json.loads(requests.post(url_get_token, data=data).text)["token"]}'}

    return headers


@pytest.fixture(scope="session", autouse=True)
def user_session(header_w_user_auth_token):
    """Get headers with Session auth using user's credentials"""

    s = requests.Session()
    s.headers = header_w_user_auth_token

    return s


@pytest.fixture
def create_book(header_w_user_auth_token):
    """Create a book via REST"""

    data = {"title": title, "author": author}  # request body
    response = requests.post(f'{url_books2}', data=data, headers=header_w_user_auth_token)

    return response  # REST response


@pytest.fixture(autouse=True)
def check_delete_book_role(user_session):
    """TearDown fixture: deletes a book, a role created in tests, by searching the book, role using key words"""
    yield
    r = json.loads(user_session.get(url_books2).text)  # get a dictionary with books

    for book in r:  # iterate through all books
        if title in book.values() or title_updated in book.values():  # search a book by name
            book_id = book['id']  # get a book id (used further to delete a book)
            user_session.delete(f'{url_books2}/{book_id}')  # delete a book by id
            print(f'Book {book_id} is deleted.')  # print a deleted book

    roles = json.loads(user_session.get(url_roles2).text)  # response - is a list of roles (dictionaries)

    for role in roles:  # iterate through all roles
        if role_name in role.values() or role_name_updated in role.values():  # search a role by name
            role_id = role['id']  # get a role id (used further to delete a role)
            user_session.delete(f'{url_roles2}/{role_id}')
            print(f'Role {role_id} is deleted.')
