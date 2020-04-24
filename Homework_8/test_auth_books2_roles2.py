from Homework_8.vars import *
import requests
import pytest


def test_get_books2_auth_no():
    """Check that no auth is needed to read books2"""

    response = requests.get(url_books2)

    assert response.status_code == 200
    assert response.reason == ok


# check both books2 and roles2 endpoints
@pytest.mark.parametrize("url", url_books2_roles2, ids=[str(item) for item in url_books2_roles2])
def test_get_books2_roles_2_auth_basic(basic_http_auth, url):  # use fixture for Basic HTTP auth generation
    """Check that Basic HTTP Auth is Ok to read books2, roles2"""

    response = requests.get(url, auth=basic_http_auth)

    assert response.status_code == 200
    assert response.reason == ok


# check both books2 and roles2 endpoints
@pytest.mark.parametrize("url", url_books2_roles2, ids=[str(item) for item in url_books2_roles2])
def test_get_books2_roles2_auth_token(header_w_user_auth_token, url):  # use fixture for Token Auth generation
    """Check that Token Auth is Ok to read books2, roles2"""

    response = requests.get(url, headers=header_w_user_auth_token)

    assert response.status_code == 200
    assert response.reason == ok


# check both books2 and roles2 endpoints
@pytest.mark.parametrize("url", url_books2_roles2, ids=[str(item) for item in url_books2_roles2])
def test_get_books2_roles2_auth_session(user_session, url):  # use session fixture
    """Check that Session Auth is Ok to read books2, roles2"""

    response = user_session.get(url)

    assert response.status_code == 200
    assert response.reason == ok


def test_get_roles2_without_auth():
    """Checks that roles2 is not available without auth"""

    response = requests.get(url_roles2)

    assert response.status_code == 403
    assert response.reason == forbidden
    assert response.text == auth_no


@pytest.mark.parametrize("auth", auth_invalid, ids=[str(item) for item in auth_invalid])
def test_get_roles_with_wrong_creds(auth):
    """Checks that roles2 is not available with wrong credentials in Basic HTTP auth"""

    response = requests.get(url_roles2, auth=("username", "password"))

    assert response.status_code == 403
    assert response.reason == forbidden
    assert response.text == invalid_user_pass


def test_get_roles_with_expired_token():
    """Checks that roles2 is not available with expired Token"""

    headers = {'Authorization': f'Token 552589d78e17333c6e78529b18303a77c15220e3'}

    response = requests.get(url_roles2, headers=headers)

    assert response.status_code == 403
    assert response.reason == forbidden
    assert response.text == token_invalid


def test_get_roles_with_wrong_token_header():
    """Checks that roles2 is not available with wrong Token header"""

    headers = {'Authorization': f'Token'}

    response = requests.get(url_roles2, headers=headers)

    assert response.status_code == 403
    assert response.reason == forbidden
    assert response.text == token_invalid_header
