from Homework_7.Book import Book
from Homework_7.Role import Role
from HtmlTestRunner import HTMLTestRunner
import unittest
import json
import requests

null = None

b = Book('http://pulse-rest-testing.herokuapp.com/')  # create Book Class object
rl = Role('http://pulse-rest-testing.herokuapp.com/')  # create Role Class object


class TestCreateBook(unittest.TestCase):
    """Book creating tests"""

    def tearDown(self):
        """Deletes a book, created in tests, by searching a book using key words"""

        response = json.loads(b.get_all_books().text)  # get all books (in form of dictionaries)

        for book in response:  # iterate through all books
            if 'test_title' in book.values():  # search a book by name
                book_id = book['id']  # get a book id (used further to delete a book)
                b.delete_book(book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_create_valid_book(self):
        """Checks book creating with valid values"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        self.assertEqual(response.status_code, 201)  # check status code
        self.assertEqual(response.reason, 'Created')  # check response message
        self.assertEqual(response.text, '{"id":' + str(book_id) + ',"title":"test_title","author":"test_author"}')

    def test_check_created_book_by_id(self):
        """Checks a created book by id in URL"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        self.assertEqual(b.find_book_by_id(book_id).status_code, 200)  # check status code
        self.assertEqual(b.find_book_by_id(book_id).reason, 'OK')  # check response message
        self.assertEqual(b.find_book_by_id(book_id).text, '{"id":' + str(book_id) + ',"title":"test_title",'
                                                                                    '"author":"test_author"}')

    def test_check_created_book_in_books_list(self):
        """Checks a created book in a books list"""

        b.create_book("test_title", "test_author")  # create a valid book
        response = json.loads(b.get_all_books().text)  # response - is a list of books (dictionaries)
        book = None

        for book in response:
            if 'test_title' and "test_author" in book.values():  # check that created book data is in response
                book = True
        self.assertTrue(book)

    def test_create_book_with_null_in_values(self):
        """Checks book creating with null values"""

        data = {"title": null, "author": null}  # request body

        response = requests.post(b.url + 'books', data=data)  # send a request
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.reason, 'Bad Request')  # check response message
        self.assertEqual(response.text, '{"title":["This field is required."],"author":["This field is required."]}')

    def test_create_book_with_empty_values(self):
        """Checks book creating with '' values"""

        response = b.create_book("", "")   # create a book with empty values
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.reason, 'Bad Request')  # check response message
        self.assertEqual(response.text, '{"title":["This field may not be blank."],'
                                        '"author":["This field may not be blank."]}')

    def test_create_book_without_title(self):
        """Checks book creating without title"""

        data = {"author": 'test_author'}  # request body

        response = requests.post(b.url+"/books", data=data)
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.reason, 'Bad Request')  # check response message
        self.assertEqual(response.text, '{"title":["This field is required."]}')

    def test_create_book_without_author(self):
        """Checks book creating without author"""

        data = {"title": 'test_title'}  # request body

        response = requests.post(b.url+"/books", data=data)
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.reason, 'Bad Request')  # check response message
        self.assertEqual(response.text, '{"author":["This field is required."]}')

    def test_create_book_without_body(self):
        """Checks book creating without body"""

        response = requests.post(b.url+"/books")
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.reason, 'Bad Request')  # check response message
        self.assertEqual(response.text, '{"title":["This field is required."],"author":["This field is required."]}')

    def test_create_book_with_reversed_body(self):
        """Checks book creating with reversed body"""

        data = {"author": "test_author", "title": "test_title"}  # request body

        response = requests.post(b.url+"/books", data=data)  # send a request
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        self.assertEqual(response.status_code, 201)  # check status code
        self.assertEqual(response.reason, 'Created')  # check response message
        self.assertEqual(response.text, '{"id":' + str(book_id) + ',"title":"test_title","author":"test_author"}')

    def test_create_book_with_invalid_keys_in_body(self):
        """Checks book creating with invalid keys"""

        data = {"title_1": "test_title", "author_1": "test_author"}

        response = requests.post(b.url+"/books", data=data)  # send a request
        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.reason, 'Bad Request')  # check response message
        self.assertEqual(response.text, '{"title":["This field is required."],"author":["This field is required."]}')

    def test_create_book_with_duplicated_values_in_body(self):
        """Tests book creating with duplicated values"""

        data = {"title": "test_title", "author": "test_author", "title": "test_title_2", "author": "test_author_2"}

        response = requests.post(b.url+"/books", data=data)  # send a request
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        self.assertEqual(response.status_code, 201)  # check status code
        self.assertEqual(response.reason, 'Created')  # check response message
        self.assertEqual(response.text, '{"id":' + str(book_id) + ',"title":"test_title_2","author":"test_author_2"}')


class TestUpdateBook(unittest.TestCase):
    """Updating book tests"""

    def tearDown(self):
        """Deletes a book, created in tests, by searching a book using key words"""

        response = json.loads(b.get_all_books().text)  # get all books (in form of dictionaries)

        for book in response:  # iterate through all books
            if 'test_title' in book.values() or 'test_title_updated' in book.values():  # search a book by name
                book_id = book['id']  # get a book id (used further to delete a book)
                b.delete_book(book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_update_book(self):
        """Checks whether a book is updated"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        # update a book
        response = b.update_book('test_title_updated', 'test_author_updated', book_id)  # update a book

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertEqual(response.text, '{"id":' + str(book_id) + ',"title":"test_title_updated",'
                                                                  '"author":"test_author_updated"}')


class TestDeleteBook(unittest.TestCase):
    """Deleting book tests"""

    def tearDown(self):
        """Deletes a book, created in tests, by searching a book using key words"""

        response = json.loads(b.get_all_books().text)  # get all books (in form of dictionaries)

        for book in response:  # iterate through all books
            if 'test_title' in book.values():  # search a book by name
                book_id = book['id']  # get a book id (used further to delete a book)
                b.delete_book(book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_delete_book(self):
        """Checks whether a book is deleted"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert

        response = b.delete_book(book_id)  # delete a book by id
        self.assertEqual(response.status_code, 204)  # check status code
        self.assertEqual(response.reason, 'No Content')  # check response message
        self.assertEqual(b.find_book_by_id(book_id).text, '{"detail":"Not found."}')


class TestCreateRole(unittest.TestCase):
    """Role creating tests"""

    def tearDown(self):
        """Deletes a role, created in tests"""

        roles = json.loads(rl.get_all_roles().text)  # response - is a list of roles (dictionaries)
        for role in roles:  # iterate through all roles
            if 'test_name' in role.values():  # search a role by name
                role_id = role['id']  # get a role id (used further to delete a role)
                rl.delete_role(role_id)
                print(f'Role {role_id} is deleted.')

        books = json.loads(b.get_all_books().text)  # get all books (in form of dictionaries)

        for book in books:  # iterate through all books
            if 'test_title' in book.values():  # search a book by name
                book_id = book['id']  # get a book id (used further to delete a book)
                b.delete_book(book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_create_role_w_valid_book(self):
        """Checks role creating with valid values and a created book"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        response = rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id

        self.assertEqual(response.status_code, 201)  # check status code
        self.assertEqual(response.reason, 'Created')  # check response message
        self.assertEqual(response.text, '{"id":' + str(role_id) + ',"name":"test_name","type":"test_type",'
                                                                  '"level":1,"book":"' + book_url + '"}')

    def test_check_created_role_by_id(self):
        """Checks a created role by id in URL"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        response = rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id

        response = rl.find_role_by_id(role_id)  # find a role by id

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertEqual(response.text, '{"id":' + str(role_id) + ',"name":"test_name","type":"test_type",'
                                        '"level":1,"book":"' + book_url + '"}')

    def test_check_created_role_in_role_list(self):
        """Checks a created role in a roles list"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        rl.create_role("test_name", "test_type", 1, book_url)  # create a role

        response = json.loads(rl.get_all_roles().text)  # response - is a list of roles (dictionaries)
        role = None

        for role in response:
            if 'test_name' and "test_type" in role.values():
                role = True
        self.assertTrue(role)

    def test_create_role_with_not_existed_book(self):
        """Tests role creating with valid values and not existed book"""

        data = {"name": "test_name", "type": "test_type", "level": 1, "book": "https://google.com"}  # request body

        response = requests.post(rl.url+"roles", data=data)  # send a request

        self.assertEqual(response.status_code, 400)  # check status code
        self.assertEqual(response.reason, 'Bad Request')  # check response message
        self.assertEqual(response.text, '{"book":["Invalid hyperlink - No URL match."]}')


class TestUpdateRole(unittest.TestCase):
    """Role updating tests"""

    def tearDown(self):
        """Deletes a role, created in tests"""

        roles = json.loads(rl.get_all_roles().text)  # response - is a list of roles (dictionaries)
        for role in roles:  # iterate through all roles
            if 'test_name' in role.values() or 'test_name_updated' in role.values():  # search a role by name
                role_id = role['id']  # get a role id (used further to delete a role)
                rl.delete_role(role_id)
                print(f'Role {role_id} is deleted.')

        books = json.loads(b.get_all_books().text)  # get all books (in form of dictionaries)

        for book in books:  # iterate through all books
            if 'test_title' in book.values():  # search a book by name
                book_id = book['id']  # get a book id (used further to delete a book)
                b.delete_book(book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_update_role(self):
        """Checks whether a role is updated"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        response = rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id

        response = rl.update_role('test_name_updated', 'test_type_updated', 2, book_url, role_id)  # update a role
        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertEqual(response.text, '{"id":' + str(role_id) + ',"name":"test_name_updated",'
                                        '"type":"test_type_updated","level":2,"book":"' + book_url + '"}')


class TestDeleteRole(unittest.TestCase):
    """Role deleting tests"""

    def tearDown(self):
        """Deletes a role, created in tests"""

        roles = json.loads(rl.get_all_roles().text)  # response - is a list of roles (dictionaries)
        for role in roles:  # iterate through all roles
            if 'test_name' in role.values():  # search a role by name
                role_id = role['id']  # get a role id (used further to delete a role)
                rl.delete_role(role_id)
                print(f'Role {role_id} is deleted.')

        books = json.loads(b.get_all_books().text)  # get all books (in form of dictionaries)

        for book in books:  # iterate through all books
            if 'test_title' in book.values():  # search a book by name
                book_id = book['id']  # get a book id (used further to delete a book)
                b.delete_book(book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_delete_role(self):
        """Checks whether a book is deleted"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        response = rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        role_id = json.loads(response.text)["id"]  # get a role_id

        response = rl.delete_role(role_id)

        self.assertEqual(response.status_code, 204)  # check status code
        self.assertEqual(response.reason, 'No Content')  # check response message
        self.assertEqual(rl.find_role_by_id(role_id).text, '{"detail":"Not found."}')


class TestRoleFilter(unittest.TestCase):
    """Checks filters"""

    def tearDown(self):
        """Deletes a role, created in tests"""

        roles = json.loads(rl.get_all_roles().text)  # response - is a list of roles (dictionaries)
        for role in roles:  # iterate through all roles
            if 'test_name' in role.values() or 'test_name_updated' in role.values():  # search a role by name
                role_id = role['id']  # get a role id (used further to delete a role)
                rl.delete_role(role_id)
                print(f'Role {role_id} is deleted.')

        books = json.loads(b.get_all_books().text)  # get all books (in form of dictionaries)

        for book in books:  # iterate through all books
            if 'test_title' in book.values():  # search a book by name
                book_id = book['id']  # get a book id (used further to delete a book)
                b.delete_book(book_id)  # delete a book by id
                print(f'Book {book_id} is deleted.')  # print a deleted book

    def test_get_role_by_book_id_filter(self):
        """Checks role filter"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        role = rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        response = rl.get_role_from_book(book_id)  # get a role from book by book id

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertEqual(response.text, f'[{role.text}]')

    def test_get_role_by_type_filter(self):
        """Checks type filter"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        role = rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        response = rl.get_role_by_type('test_type')  # get a role by role type

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertEqual(response.text, f'[{role.text}]')

    def test_get_role_by_level_filter(self):
        """Checks level filter"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        response = rl.get_role_by_level(1)  # get a role by role level
        print(response.text)

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertIn('"level":1', response.text)

    def test_get_role_less_than_filter_value(self):
        """Checks roles by role filter"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        rl.create_role("test_name", "test_type", 0, book_url)  # create a role
        response = rl.get_role_by_level_param(level_lt='1')  # get all roles less than specified role level

        sorted_response = sorted(json.loads(response.text), key=lambda dictionary: dictionary['level'])
        min_role_level = (sorted_response[0]['level'])  # get min role level

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertLess(min_role_level, 1)

    def test_get_role_less_equal_than_filter_value(self):
        """Checks roles by role filter"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        response = rl.get_role_by_level_param(level_lte='1')  # get all roles less than specified role level

        sorted_response = sorted(json.loads(response.text), key=lambda dictionary: dictionary['level'])
        min_role_level = (sorted_response[0]['level'])  # get min role level

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertLessEqual(min_role_level, 1)

    def test_get_role_greater_than_filter_value(self):
        """Checks roles by role filter"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        response = rl.get_role_by_level_param(level_gt='1')  # get all roles less than specified role level

        sorted_response = sorted(json.loads(response.text), key=lambda dictionary: dictionary['level'])
        min_role_level = (sorted_response[0]['level'])  # get min role level

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertGreater(min_role_level, 1)

    def test_get_role_greater_equal_than_filter_value(self):
        """Checks roles by role filter"""

        response = b.create_book("test_title", "test_author")  # create a valid book
        book_id = json.loads(response.text)["id"]  # get a book id for assert
        book_url = rl.url + "books/" + str(book_id)  # create a book URL

        rl.create_role("test_name", "test_type", 1, book_url)  # create a role
        response = rl.get_role_by_level_param(level_gte='1')  # get all roles less than specified role level

        sorted_response = sorted(json.loads(response.text), key=lambda dictionary: dictionary['level'])
        min_role_level = (sorted_response[0]['level'])  # get min role level

        self.assertEqual(response.status_code, 200)  # check status code
        self.assertEqual(response.reason, 'OK')  # check response message
        self.assertGreaterEqual(min_role_level, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='/home/galgo/PycharmProjects/d_zhyvov_test'
                                                                '/Homework_7/test_report'))
