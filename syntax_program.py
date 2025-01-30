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

# Функция для получения списка синтаксических конструкций для каждого языка
def get_syntax_constructions_by_language(languages, syntax_constructions):
    sorted_languages = sorted(languages, key=lambda lang: lang.name)
    result = {}
    for lang in sorted_languages:
        constructs = [syn.name for syn in syntax_constructions if syn.language_id == lang.id]
        result[lang.name] = constructs
    return result

# Функция для подсчета количества синтаксических конструкций для каждого языка
def get_language_syntax_count(languages, syntax_constructions):
    language_counts = {
        lang.name: sum(1 for syn in syntax_constructions if syn.language_id == lang.id)
        for lang in languages
    }
    return language_counts

# Функция для фильтрации языков, содержащих слово "язык" в названии
def get_filtered_languages(languages, syntax_constructions):
    filtered_languages = [lang for lang in languages if "язык" in lang.name.lower()]
    result = {}
    for lang in filtered_languages:
        constructs = [syn.name for syn in syntax_constructions if syn.language_id == lang.id]
        result[lang.name] = constructs
    return result

