from flask import url_for


class TestPosts(object):
    def test_post_page(self,client):
        """Post page should respond with a 200"""
        response = client.get(url_for('mypost.post'))
        assert response.status_code == 200

    def test_post_update_page(self,client):
        """Post update page should respond with a 200"""
        response = client.get(url_for('mypost.update'))
        assert response.status_code == 200

    def test_post_delete_page(self,client):
        """Post delete route should respond with a 200"""
        response = client.get(url_for('mypost.delete', id = 1))
        assert response.status_code == 200
    
    def test_post_form(self,client):
        """Post form should redirect with a message"""
        form = {
            'body':'Testing post form'
        }
        response = client.post(url_for('mypost.post'), data=form,
                                follow_redirects=True)
        assert response.status_code == 200

    
    def test_post_update_form(self,client):
        """Post update form should redirect with a message"""
        form = {
            'body':'Testing post form'
        }
        response = client.post(url_for('mypost.update',id =1), data=form,
                                follow_redirects=True)
        assert response.status_code == 200
