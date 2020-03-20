from flask import url_for

from lib.tests import assert_status_with_message


class TestUsers(object):
    
        def test_signup_page(self,client):
            """Users registration page should respond with a 200"""
            response = client.get(url_for('user.signup'))
            assert response.status_code == 200

        def test_signup_form(self,client):
            """Registration form should redirect with a message"""
            form = {
                'username':'testuser',
                'email':'testuser@gmail.com',
                'firstname':'test',
                'lastname':'user',
                'password':'passtestuser'
            }
            response = client.post(url_for('user.signup'), data=form,
                               follow_redirects=True)
            assert response.status_code == 200

        def test_login_page(self,client):
            """Login page should respond with a 200"""
            response = client.get(url_for('user.login'))
            assert response.status_code == 200

        def test_login_form(self,client):
            """Login form should redirect with a message"""
            form = {
                'email':'newuser@gmail.com',
                'password':'passmenow'
            }
            response = client.post(url_for('user.login'), data=form,
                                follow_redirects=True)
            assert response.status_code == 200