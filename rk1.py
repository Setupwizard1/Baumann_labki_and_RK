class SyntaxConstruction:
    def __init__(self, id, name, language_id):
        self.id = id
        self.name = name
        self.language_id = language_id

class ProgrammingLanguage:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LanguageSyntax:
    def __init__(self, syntax_id, language_id):
        self.syntax_id = syntax_id
        self.language_id = language_id

# Создание тестовых данных
languages = [
    ProgrammingLanguage(1, "Python"),
    ProgrammingLanguage(2, "Java"),
    ProgrammingLanguage(3, "C++")
]

syntax_constructions = [
    SyntaxConstruction(1, "if-else", 1),
    SyntaxConstruction(2, "for loop", 1),
    SyntaxConstruction(3, "while loop", 2),
    SyntaxConstruction(4, "switch-case", 3),
    SyntaxConstruction(5, "try-catch", 2)
]

language_syntax = [
    LanguageSyntax(1, 1), LanguageSyntax(2, 1),
    LanguageSyntax(3, 2), LanguageSyntax(4, 3),
    LanguageSyntax(5, 2)
]

# Запрос 1: Список всех связанных синтаксических конструкций и языков, отсортированных по языкам
sorted_languages = sorted(languages, key=lambda lang: lang.name)
for lang in sorted_languages:
    constructs = [syn.name for syn in syntax_constructions if syn.language_id == lang.id]
    print(f"{lang.name}: {', '.join(constructs)}")

# Запрос 2: Список языков с количеством конструкций
language_counts = {
    lang.name: sum(1 for syn in syntax_constructions if syn.language_id == lang.id)
    for lang in languages
}
print(sorted(language_counts.items(), key=lambda x: x[1], reverse=True))

# Запрос 3: Языки, содержащие "язык" и их конструкции
filtered_languages = [lang for lang in languages if "язык" in lang.name.lower()]
for lang in filtered_languages:
    constructs = [syn.name for syn in syntax_constructions if syn.language_id == lang.id]
    print(f"{lang.name}: {', '.join(constructs)}")
