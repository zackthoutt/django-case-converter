from unittest.case import TestCase
from unittest import main
from case_converter.utils import convert_to_camel_case, convert_to_underscore


class TestConvertToCamelCase(TestCase):
    def test_underscore_to_camel_dict(self):
        input_data = {
            "9_under_score_4_days": 1,
            "a_game_of_thrones": 1
        }
        expected_output = {
            "9UnderScore4Days": 1,
            "aGameOfThrones": 1
        }
        test_output = convert_to_camel_case(input_data)
        self.assertEqual(test_output, expected_output)

    def test_underscore_to_camel_list(self):
        input_data = [
            {
                "9_under_score_4_days": 1,
                "a_game_of_thrones": 1
            }
        ]
        expected_output = [
            {
                "9UnderScore4Days": 1,
                "aGameOfThrones": 1
            }
        ]
        test_output = convert_to_camel_case(input_data)
        self.assertEqual(test_output, expected_output)

    def test_underscore_to_camel_tuple(self):
        input_data = (
            {
                "9_under_score_4_days": 1,
                "a_game_of_thrones": 1
            }
        )
        expected_output = (
            {
                "9UnderScore4Days": 1,
                "aGameOfThrones": 1
            }
        )
        test_output = convert_to_camel_case(input_data)
        self.assertEqual(test_output, expected_output)

    def test_underscore_to_camel_str(self):
        input_data = "A test string"
        test_output = convert_to_camel_case(input_data)
        self.assertEqual(test_output, input_data)

    def test_underscore_to_camel_nested(self):
        input_data = {
            "an_underscore_item": 1,
            "an_underscore_dict": {
                "an_underscore_item": 1,
            },
            "an_underscore_list": [
                {
                    "an_underscore_item": 1,
                },
            ],
            "an_underscore_tuple": (
                {
                    "an_underscore_item": 1,
                },
            )
        }
        expected_output = {
            "anUnderscoreItem": 1,
            "anUnderscoreDict": {
                "anUnderscoreItem": 1,
            },
            "anUnderscoreList": [
                {
                    "anUnderscoreItem": 1,
                },
            ],
            "anUnderscoreTuple": (
                {
                    "anUnderscoreItem": 1,
                },
            )
        }
        test_output = convert_to_camel_case(input_data)
        self.assertEqual(test_output, expected_output)


class TestConvertToUnderscore(TestCase):
    def test_camel_to_underscore_dict(self):
        input_data = {
            "9UnderScore4Days": 1,
            "aGameOfThrones": 1
        }
        expected_output = {
            "9_under_score_4_days": 1,
            "a_game_of_thrones": 1
        }
        test_output = convert_to_underscore(input_data)
        self.assertEqual(test_output, expected_output)

    def test_camel_to_underscore_list(self):
        input_data = [
            {
                "9UnderScore4Days": 1,
                "aGameOfThrones": 1
            }
        ]
        expected_output = [
            {
                "9_under_score_4_days": 1,
                "a_game_of_thrones": 1
            }
        ]
        test_output = convert_to_underscore(input_data)
        self.assertEqual(test_output, expected_output)

    def test_camel_to_underscore_tuple(self):
        input_data = (
            {
                "9UnderScore4Days": 1,
                "aGameOfThrones": 1
            }
        )
        expected_output = (
            {
                "9_under_score_4_days": 1,
                "a_game_of_thrones": 1
            }
        )
        test_output = convert_to_underscore(input_data)
        self.assertEqual(test_output, expected_output)

    def test_camel_to_underscore_str(self):
        input_data = "A test string"
        test_output = convert_to_underscore(input_data)
        self.assertEqual(test_output, input_data)

    def test_camel_to_underscore_nested(self):
        input_data = {
            "anUnderscoreItem": 1,
            "anUnderscoreDict": {
                "anUnderscoreItem": 1,
            },
            "anUnderscoreList": [
                {
                    "anUnderscoreItem": 1,
                },
            ],
            "anUnderscoreTuple": (
                {
                    "anUnderscoreItem": 1,
                },
            )
        }
        expected_output = {
            "an_underscore_item": 1,
            "an_underscore_dict": {
                "an_underscore_item": 1,
            },
            "an_underscore_list": [
                {
                    "an_underscore_item": 1,
                },
            ],
            "an_underscore_tuple": (
                {
                    "an_underscore_item": 1,
                },
            )
        }
        test_output = convert_to_underscore(input_data)
        self.assertEqual(test_output, expected_output)


if __name__ == '__main__':
    main()
