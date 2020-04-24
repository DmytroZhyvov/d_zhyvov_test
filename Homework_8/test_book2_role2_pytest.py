import requests
import pytest
import json
from Homework_8.vars import *


@pytest.mark.parametrize('data', data_valid_various, ids=[str(item) for item in data_valid_various])
def test_create_valid_book(user_session, data):    # use fixture for token generation
    """Checks book creating with valid values in different order"""

    response = user_session.post(url_books2, data=data)  # send a request

    print(json.loads(response.text)["id"])
    assert response.status_code == 201  # check status code
    assert response.reason == created  # check response message
    assert json.loads(response.text) == {"id": json.loads(response.text)["id"], "title": title, "author": author}


def test_check_created_book_by_id(create_book):  # use fixture for book creating
    """Checks a created book by id in URL"""

    book_id = json.loads(create_book.text)["id"]  # get a book id for checking
    response = requests.get(f'{url_books2}/{book_id}')  # send a request with book id

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert json.loads(response.text) == {"id": book_id, "title": title, "author": author}


def test_check_created_book_in_books_list(create_book):  # use fixture for book creating
    """Checks a created book in a books list"""

    b = create_book  # create a book
    response = requests.get(url_books2)  # send a request to get all books

    titles = [book['title'] for book in json.loads(response.text)]  # create a list of all book titles

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert title in titles  # check that test book title is among all books title


@pytest.mark.parametrize('data', data_null_no, ids=[str(item) for item in data_null_no])
def test_create_book_with_null_no_invalid_body(user_session, data):
    """Checks book creating with null values, without body, invalid keys"""

    response = user_session.post(url_books2, data=data)  # send a request

    assert response.status_code == 400  # check status code
    assert response.reason == bad_request  # check response message
    assert response.text == title_author_required


def test_create_book_with_empty_values(user_session):
    """Checks book creating with '' values"""

    data = {"title": "", "author": ""}  # request body

    response = user_session.post(url_books2, data=data)  # send a request

    assert response.status_code == 400  # check status code
    assert response.reason == bad_request  # check response message
    assert response.text == title_author_blank


def test_create_book_without_title(user_session):
    """Checks book creating without title"""

    data = {"author": author}  # request body

    response = user_session.post(url_books2, data=data)  # send a request

    assert response.status_code == 400  # check status code
    assert response.reason == bad_request  # check response message
    assert response.text == title_required


def test_create_book_without_author(user_session):
    """Checks book creating without author"""

    data = {"title": title}  # request body

    response = user_session.post(url_books2, data=data)  # send a request

    assert response.status_code == 400  # check status code
    assert response.reason == bad_request  # check response message
    assert response.text == author_required


def test_update_valid_book(user_session):
    """Checks whether a valid book is updated"""

    # create a book and get a book id for updating
    book_id = json.loads(user_session.post(url_books2, data=book_data).text)["id"]

    data = {"title": title_updated, "author": author_updated}  # body for updating book request

    response = user_session.put(f'{url_books2}/{book_id}', data=data)

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert json.loads(response.text) == {"id": json.loads(response.text)["id"], "title": title_updated,
                                         "author": author_updated}


def test_delete_book(user_session):
    """Checks whether a book is deleted"""

    # create a book and get a book id for deleting
    book_id = json.loads(user_session.post(url_books2, data={"title": title, "author": author}).text)["id"]

    response = user_session.delete(f'{url_books2}/{book_id}')  # delete a book by id
    assert response.status_code == 204  # check status code
    assert response.reason == no_content  # check response message
    assert requests.get(f'{url_books2}/{book_id}').text == not_found


def test_create_role_w_valid_book(user_session):
    """Checks role creating with valid values and a created book"""

    # create a valid book and get book id
    book_id = json.loads(user_session.post(f'{url_books2}', data=book_data).text)["id"]

    data = {"name": role_name, "type": role_type, "level": 1, "book": book_id}  # role body

    response = user_session.post(url_roles2, data=data)  # create a role

    role_id = json.loads(response.text)["id"]  # get a role_id

    assert response.status_code == 201  # check status code
    assert response.reason == created  # check response message
    assert json.loads(response.text) == {"id": role_id, "name":role_name, "type": role_type, "level": 1,"book": book_id}


def test_check_created_role_by_id(user_session):
    """Checks a created role by id in URL"""

    # create a valid book and get book id
    book_id = json.loads(user_session.post(f'{url_books2}', data=book_data).text)["id"]

    data = {"name": role_name, "type": role_type, "level": 1, "book": book_id}  # role body

    response = user_session.post(url_roles2, data=data)  # create a role

    role_id = json.loads(response.text)["id"]  # get a role_id

    response = user_session.get(f'{url_roles2}/{role_id}')  # find a role by id

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert json.loads(response.text) == {"id": role_id, "name":role_name, "type": role_type, "level": 1,"book": book_id}


def test_check_created_role_in_role_list(create_book):
    """Checks a created role in a roles list"""

    book_id = json.loads(create_book.text)["id"]  # create a book and get a book id

    data = {"name": role_name, "type": role_type, "level": 1, "book": book_id}  # role body

    requests.post(url_roles2, data=data, auth=(username, password))  # create a role

    response = requests.get(url_roles2, auth=(username, password))  # get all roles

    roles = [role["name"] for role in json.loads(response.text)]  # create a list of all role names

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert role_name in roles  # check that test role name is among all roles names


def test_create_role_with_not_existed_book(user_session):
    """Tests role creating with valid values and not existed book"""

    data = {"name": role_name, "type": role_type, "level": 1, "book": 0}  # request body

    response = user_session.post(url_roles2, data=data)  # send a request

    assert response.status_code == 400  # check status code
    assert response.reason == bad_request  # check response message
    assert response.text == object_not_exist


def test_update_role(user_session):
    """Checks whether a role is updated"""

    # create a valid book and get book id
    book_id = json.loads(user_session.post(f'{url_books2}', data=book_data).text)["id"]

    data = {"name": role_name, "type": role_type, "level": 1, "book": book_id}  # role body

    response = user_session.post(url_roles2, data=data)  # create a role

    role_id = json.loads(response.text)["id"]  # get a role_id

    data = {"name": role_name_updated, "type": role_type, "level": 1, "book": book_id}

    response = user_session.put(f'{url_roles2}/{role_id}', data=data)  # update a role

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert json.loads(response.text) == {"id": role_id, "name": role_name_updated, "type": role_type, "level": 1,
                                         "book": book_id}


def test_delete_role(user_session):
    """Checks whether a book is deleted"""

    # create a valid book and get book id
    book_id = json.loads(user_session.post(f'{url_books2}', data=book_data).text)["id"]

    data = {"name": role_name, "type": role_type, "level": 1, "book": book_id}  # role body

    response = user_session.post(url_roles2, data=data)  # create a role

    role_id = json.loads(response.text)["id"]  # get a role_id

    response = user_session.delete(f'{url_roles2}/{role_id}')

    assert response.status_code == 204  # check status code
    assert response.reason == no_content  # check response message


def test_get_role_by_book_id_filter(user_session):
    """Checks role filter"""

    # create a valid book and get book id
    book_id = json.loads(user_session.post(f'{url_books2}', data=book_data).text)["id"]

    data = {"name": role_name, "type": role_type, "level": 1, "book": book_id}  # role body

    role = user_session.post(url_roles2, data=data)  # create a role

    payload = {'book_id': book_id}

    response = user_session.get(url_roles2, params=payload)  # get a role from book by book id

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert response.text == f'[{role.text}]'


def test_get_role_less_than_filter_value(user_session):
    """Checks roles by role filter"""

    # create a valid book and get book id
    book_id = json.loads(user_session.post(f'{url_books2}', data=book_data).text)["id"]

    data = {"name": role_name, "type": role_type, "level": 1, "book": book_id}  # role body

    user_session.post(url_roles2, data=data)  # create a role

    payload = {'level__lt': 1}

    # get all roles less than specified role level
    response = user_session.get(url_roles2, params=payload)

    sorted_response = sorted(json.loads(response.text), key=lambda dictionary: dictionary['level'])
    min_role_level = (sorted_response[0]['level'])  # get min role level

    assert response.status_code == 200  # check status code
    assert response.reason == ok  # check response message
    assert min_role_level < 1
