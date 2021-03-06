from unittest import TestCase
from ufixtures.UfixBetamax import *

class TestUfixBetamax(TestCase):
    def setUp(self) -> None:
        session = Session()
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.ufixtures = UfixBetamax(session, os.path.join(curr_dir, 'fixtures/cassettes'))

    def test__sanitizer_factory(self):
        hook = self.ufixtures._sanitizer_factory("Authorization")
        self.assertTrue(isinstance(hook, Callable))

    def test_sanitize(self):
        vcr = self.ufixtures.sanitize("Authorization")
        self.assertTrue(isinstance(vcr, Betamax))