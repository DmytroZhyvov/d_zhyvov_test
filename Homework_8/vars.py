# URLS
url_basic = "http://pulse-rest-testing.herokuapp.com"
url_get_token = f"{url_basic}/api-token-auth/"
url_books2 = f"{url_basic}/books2"
url_roles2 = f"{url_basic}/roles2"

url_books2_roles2 = [
    f"{url_basic}/books2",
    f"{url_basic}/roles2"
]


# User's credentials
username = "Dz"
password = "110285"

# Invalid User's credentials
auth_invalid = [
    ("username", "password"),
    (username, "password"),
    ("username", password),
    ("", ""),
    (username, ""),
    ("", password),
    (None, None),
    ()
]

# Book variables
title = "test_title"
title_updated = "test_title_updated"
author = "test_author"
author_updated = "test_author_updated"
book_data = {"title": title, "author": author}

# Role variables
role_name = "role_name"
role_name_updated = "role_name_updated"
role_type = "role_type"
role_level = "role_level"

# Request body
data_valid_various = [
    {"title": title, "author": author},
    {"author": author, "title": title}
]

data_null_no = [
    {"title": None, "author": None},
    {},
    {"title_1": title, "author_1": author}
]

# API Response reasons
ok = 'OK'
created = "Created"
forbidden = "Forbidden"
token_invalid = '{"detail":"Invalid token."}'
token_invalid_header = '{"detail":"Invalid token header. No credentials provided."}'
bad_request = "Bad Request"
author_required = '{"author":["This field is required."]}'
title_required = '{"title":["This field is required."]}'
title_author_required = '{"title":["This field is required."],"author":["This field is required."]}'
title_author_blank = '{"title":["This field may not be blank."],"author":["This field may not be blank."]}'
no_content = "No Content"
not_found = '{"detail":"Not found."}'
auth_no = '{"detail":"Authentication credentials were not provided."}'
invalid_user_pass = '{"detail":"Invalid username/password."}'
object_not_exist = '{"book":["Invalid pk \\"0\\" - object does not exist."]}'



