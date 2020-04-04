import requests


class Book:
    """Main Book class"""

    def __init__(self, url):
        """Constructor"""
        self.url = url  # base URL

    def create_book(self, title, author):
        """Create a book via REST"""

        url = self.url + 'books'  # request URL
        data = {"title": title, "author": author}  # request body
        response = requests.post(url, data)  # send a post request with a payload

        return response  # REST response

    def update_book(self, title, author, book_id=None):
        """Update a book via REST"""

        url = self.url + 'books/' + str(book_id)  # form an API endpoint
        data = {"title": title, "author": author}  # request body
        response = requests.put(url, data)  # send a put request with a payload

        return response  # REST response

    def delete_book(self, book_id=None):
        """Delete a book via REST by book id"""

        url = self.url + 'books/' + str(book_id)  # form an API endpoint
        response = requests.delete(url)  # send a delete request

        return response

    def find_book_by_id(self, book_id=None):
        """Find a book via REST by book id"""

        url = self.url + 'books/' + str(book_id)  # form an API endpoint
        response = requests.get(url)  # send a get request

        return response

    def get_all_books(self):
        """Get all books via REST"""

        url = self.url + 'books'  # form an API endpoint
        response = requests.get(url)  # send a get request

        return response
