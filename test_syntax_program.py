import unittest
from syntax_program import SyntaxConstruction, ProgrammingLanguage, LanguageSyntax, \
    get_syntax_constructions_by_language, get_language_syntax_count, get_filtered_languages


class TestSyntaxFunctions(unittest.TestCase):

    def setUp(self):
        # Создание тестовых данных
        self.languages = [
            ProgrammingLanguage(1, "Python"),
            ProgrammingLanguage(2, "Java"),
            ProgrammingLanguage(3, "C++")
        ]

        self.syntax_constructions = [
            SyntaxConstruction(1, "if-else", 1),
            SyntaxConstruction(2, "for loop", 1),
            SyntaxConstruction(3, "while loop", 2),
            SyntaxConstruction(4, "switch-case", 3),
            SyntaxConstruction(5, "try-catch", 2)
        ]

    def test_get_syntax_constructions_by_language(self):
        result = get_syntax_constructions_by_language(self.languages, self.syntax_constructions)
        self.assertEqual(result, {
            "C++": ["switch-case"],
            "Java": ["while loop", "try-catch"],
            "Python": ["if-else", "for loop"]
        })

    def test_get_language_syntax_count(self):
        result = get_language_syntax_count(self.languages, self.syntax_constructions)
        self.assertEqual(result, {
            "Python": 2,
            "Java": 2,
            "C++": 1
        })

    def test_get_filtered_languages(self):
        result = get_filtered_languages(self.languages, self.syntax_constructions)
        self.assertEqual(result, {})

        # Добавляем язык с "язык" в названии и связываем синтаксические конструкции
        self.languages.append(ProgrammingLanguage(4, "Russian язык"))
        self.syntax_constructions.append(SyntaxConstruction(6, "if-else", 4))
        self.syntax_constructions.append(SyntaxConstruction(7, "for loop", 4))

        result = get_filtered_languages(self.languages, self.syntax_constructions)
        self.assertEqual(result, {
            "Russian язык": ["if-else", "for loop"]
        })


if __name__ == "__main__":
    unittest.main()
