import unittest

from src.submission_guard import SubmissionGuard


class SubmissionGuardTest(unittest.TestCase):
    def test_immediate_duplicate_is_rejected(self):
        guard = SubmissionGuard()

        self.assertTrue(guard.accept("request-a"))
        self.assertFalse(guard.accept("request-a"))

    def test_repeat_request_after_another_request_is_rejected(self):
        guard = SubmissionGuard()

        self.assertTrue(guard.accept("request-a"))
        self.assertTrue(guard.accept("request-b"))
        self.assertFalse(guard.accept("request-a"))


if __name__ == "__main__":
    unittest.main()
