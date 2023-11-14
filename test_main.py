import unittest

from api_test.Api_Page_Object import Api_automation as api
import pytest


class main (unittest.TestCase):

    @pytest.mark.run(order=1)
    def test_get_request(self):
        api.get_request(self)

    @pytest.mark.run(order=2)
    def test_post_request(self):
        api.post_request(self)

    @pytest.mark.run(order=3)
    def test_put_request(self):
        api.Put_request(self)

    @pytest.mark.run(order=4)
    def test_patch_request(self):
        api.Patch_request(self)

    @pytest.mark.run(order=5)
    def test_delete_request(self):
        api.delete_request(self)

    @pytest.mark.run(order=6)
    def test_InvalidAuth_request(self):
        api.invalid_Auth_request(self)

    @pytest.mark.run(order=7)
    def test_ValidAuth_request(self):
        api.valid_Auth_request(self)

    @pytest.mark.run(order=8)
    def test_ValidTimeOut_request(self):
        api.valid_timeout_request(self)

    @pytest.mark.run(order=9)
    def test_InvalidTimeOut_request(self):
        api.invalid_timeout_request(self)


