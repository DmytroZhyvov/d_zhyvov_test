from Homework_6.task_1.manage_book_role import manage_book, manage_role
import unittest
import json
import requests

null = None


class TestBooks(unittest.TestCase):
    """For tests use the following books actions:
   'create' --> to create a book
   'update' --> to change a book
   'delete' --> to delete a book
   'find_book' --> to find a book by id
   'get_books' --> to get a list of books
   """

    def tearDown(self):
        """Deletes a book, created in tests, by searching a book using key words"""

        response = json.loads((manage_book('get_books')).text)  # get all books (in form of dictionaries)

        for book in response:  # iterate through all books
            if 'test_title' in book.values() or 'test_title_updated' in book.values()\
                    or 'test_title_2' in book.values():  # search a book by name

                book_id = book['id']  # get a book id (used further to delete a book)

                manage_book(action='delete', book_id=book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_create_valid_book(self):
        """Tests book creating with valid values"""

        response = manage_book("create", "test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        self.assertEqual(response.status_code, 201)  # check status code
        self.assertEqual(response.text, '{"id":' + str(book_id) + ',"title":"test_title","author":"test_author"}')

    def test_check_created_book_by_id(self):
        """Checks a created book by id in URL"""

        response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a valid book
        book_id = response["id"]
        self.assertEqual(manage_book(action='find_book', book_id=book_id).status_code, 200)
        self.assertEqual(manage_book(action='find_book', book_id=book_id).text, '{"id":' + str(book_id) +
                         ',"title":"test_title","author":"test_author"}')

    def test_check_created_book_in_books_list(self):
        """Checks a created book in a books list"""

        manage_book("create", "test_title", "test_author")  # create a valid book
        response = json.loads(manage_book('get_books').text)  # response - is a list of books (dictionaries)
        book = None

        for book in response:
            if 'test_title' and "test_author" in book.values():
                book = True
        self.assertTrue(book)

    def test_update_book(self):
        """Checks whether a book is updated"""

        response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a valid book
        book_id = response["id"]  # get a book id

        # update a book
        response = manage_book(action="update", title='test_title_updated', author='test_author_updated',
                               book_id=book_id)  # update a book
        self.assertEqual(response.status_code, 200)
        self.assertEqual(manage_book(action='find_book', book_id=book_id).text, '{"id":' + str(book_id) +
                         ',"title":"test_title_updated","author":"test_author_updated"}')

    def test_delete_book(self):
        """Checks whether a book is deleted"""

        response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a valid book
        book_id = response["id"]  # get a book id
        response = manage_book(action='delete', book_id=book_id)  # delete a book by id
        self.assertEqual(response.status_code, 204)
        self.assertEqual(manage_book(action='find_book', book_id=book_id).text, '{"detail":"Not found."}')

    def test_create_book_with_null_in_values(self):
        """Tests book creating with null values"""

        # request payload
        data = {
            "title": null,          # null = None
            "author": null
        }

        response = requests.post("http://pulse-rest-testing.herokuapp.com/books", data=data)  # send a request
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.text, '{"title":["This field is required."],"author":["This field is required."]}')

    def test_create_book_with_empty_values(self):
        """Tests book creating with '' values"""

        response = manage_book("create", "", "")  # create a book with empty values
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.text, '{"title":["This field may not be blank."],'
                                        '"author":["This field may not be blank."]}')

    def test_create_book_without_title(self):
        """Tests book creating without title"""

        # request payload
        data = {
            "author": 'test_author'
        }

        response = requests.post("http://pulse-rest-testing.herokuapp.com/books", data=data)
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.text, '{"title":["This field is required."]}')

    def test_create_book_without_author(self):
        """Tests book creating without author"""

        # request payload
        data = {
            "title": 'test_title'
        }

        response = requests.post("http://pulse-rest-testing.herokuapp.com/books", data=data)
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.text, '{"author":["This field is required."]}')

    def test_create_book_without_body(self):
        """Tests book creating without body"""

        response = requests.post("http://pulse-rest-testing.herokuapp.com/books")
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.text, '{"title":["This field is required."],"author":["This field is required."]}')

    def test_create_book_with_reversed_body(self):
        """Tests book creating with reversed body"""

        # request payload
        data = {
            "author": "test_author",
            "title": "test_title",

        }

        response = requests.post("http://pulse-rest-testing.herokuapp.com/books", data=data)  # send a request
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        self.assertEqual(response.status_code, 201)  # check status code
        self.assertEqual(response.text, '{"id":' + str(book_id) + ',"title":"test_title","author":"test_author"}')

    def test_create_book_with_invalid_keys_in_body(self):
        """Tests book creating with invalid keys"""

        data = {  # request body
            "title_1": "test_title",
            "author_1": "test_author"

        }

        response = requests.post("http://pulse-rest-testing.herokuapp.com/books", data=data)  # send a request
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.text, '{"title":["This field is required."],"author":["This field is required."]}')

    def test_create_book_with_duplicated_values_in_body(self):
        """Tests book creating with duplicated values"""

        data = {  # request body
            "title": "test_title",
            "author": "test_author",
            "title": "test_title_2",
            "author": "test_author_2"
        }

        response = requests.post("http://pulse-rest-testing.herokuapp.com/books", data=data)  # send a request
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        self.assertEqual(response.status_code, 201)  # check status code
        self.assertEqual(response.text, '{"id":' + str(book_id) + ',"title":"test_title_2","author":"test_author_2"}')


class TestRoles(unittest.TestCase):
    """For tests use the following roles actions:
    'create' --> to create a role
    'update' --> to change a role
    'delete' --> to delete a role
    'find_role' --> to find a role by id
    'get_roles' --> to get a list of roles
   """

    def tearDown(self):
        """Deletes a book, created in tests"""

        roles = json.loads((manage_role('get_roles')).text)  # response - is a list of books (dictionaries)
        for role in roles:
            if 'test_name' in role.values() or 'test_name_updated' in role.values():
                role_id = role['id']
                manage_role(action='delete', role_id=role_id)
                print(f'Role {role_id} is deleted.')

        books = json.loads((manage_book('get_books')).text)  # response - is a list of books (dictionaries)

        for book in books:
            if 'test_title' in book.values() or 'test_title_updated' in book.values():
                book_id = book['id']

                manage_book(action='delete', book_id=book_id)
                print(f'Book {book_id} is deleted.')

    def test_create_role_w_valid_book(self):
        """Tests role creating with valid values and a created book"""

        book_response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a book
        book_id = book_response["id"]  # get a book id
        book_url = "http://pulse-rest-testing.herokuapp.com/books/" + str(book_id)  # create a book URL

        response = manage_role(action='create', role_name='test_name', role_type='test_type',
                               role_level=1, book=book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.text, '{"id":' + str(role_id) + ',"name":"test_name","type":"test_type",'
                                                                  '"level":1,"book":"' + book_url + '"}')

    def test_check_created_role_by_id(self):
        """Checks a created role by id in URL"""

        book_response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a book
        book_id = book_response["id"]  # get a book id
        book_url = "http://pulse-rest-testing.herokuapp.com/books/" + str(book_id)  # create a book URL

        response = manage_role(action='create', role_name='test_name', role_type='test_type',
                               role_level=1, book=book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id
        response = manage_role(action='find_role', role_id=role_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '{"id":' + str(role_id) + ',"name":"test_name","type":"test_type",'
                                        '"level":1,"book":"' + book_url + '"}')

    def test_check_created_role_in_role_list(self):
        """Checks a created role in a roles list"""

        book_response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a book
        book_id = book_response["id"]  # get a book id
        book_url = "http://pulse-rest-testing.herokuapp.com/books/" + str(book_id)  # create a book URL

        manage_role(action='create', role_name='test_name', role_type='test_type', role_level=1,
                    book=book_url)  # create a role
        response = json.loads(manage_role('get_roles').text)  # response - is a list of roles (dictionaries)
        role = None

        for role in response:
            if 'test_name' and "test_type" in role.values():
                role = True
        self.assertTrue(role)

    def test_update_role(self):
        """Checks whether a role is updated"""

        book_response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a book
        book_id = book_response["id"]  # get a book id
        book_url = "http://pulse-rest-testing.herokuapp.com/books/" + str(book_id)  # create a book URL

        response = manage_role(action='create', role_name='test_name', role_type='test_type',
                               role_level=1, book=book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id

        # update a role
        response = manage_role(action='update', role_name='test_name_updated', role_type='test_type_updated',
                               role_level=2, book=book_url, role_id=role_id)  # update a role
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '{"id":' + str(role_id) + ',"name":"test_name_updated",'
                                        '"type":"test_type_updated","level":2,"book":"' + book_url + '"}')

    def test_delete_role(self):
        """Checks whether a book is deleted"""

        book_response = json.loads((manage_book("create", "test_title", "test_author")).text)  # create a book
        book_id = book_response["id"]  # get a book id
        book_url = "http://pulse-rest-testing.herokuapp.com/books/" + str(book_id)  # create a book URL

        response = manage_role(action='create', role_name='test_name', role_type='test_type',
                               role_level=1, book=book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id

        response = manage_role(action='delete', role_id=role_id)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(manage_role(action='find_role', role_id=role_id).text, '{"detail":"Not found."}')

    def test_create_role_with_not_existed_book(self):
        """Tests role creating with valid values and not existed book"""

        # request body
        data = {
            "name": "test_name",
            "type": "test_type",
            "level": 1,
            "book": "https://google.com"
        }

        response = requests.post("http://pulse-rest-testing.herokuapp.com/roles", data=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, '{"book":["Invalid hyperlink - No URL match."]}')

