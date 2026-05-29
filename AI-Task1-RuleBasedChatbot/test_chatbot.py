import unittest

from chatbot import clean_text, find_response


class ChatbotTests(unittest.TestCase):
    def test_clean_text_removes_extra_spacing_and_symbols(self):
        self.assertEqual(clean_text("  Hello!!!   Bot?? "), "hello bot")

    def test_greeting_gets_response(self):
        response, should_end = find_response("hello")
        self.assertFalse(should_end)
        self.assertTrue(len(response) > 0)

    def test_bye_ends_chat(self):
        response, should_end = find_response("bye")
        self.assertTrue(should_end)
        self.assertIn(response, ["Goodbye! Have a great day.", "See you later!"])

    def test_unknown_input_uses_fallback(self):
        response, should_end = find_response("explain quantum gardening")
        self.assertFalse(should_end)
        self.assertTrue(len(response) > 0)


if __name__ == "__main__":
    unittest.main()
