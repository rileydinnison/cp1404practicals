"""
Languages
Estimate: 60 minutes
Actual:   49 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
java = ProgrammingLanguage("Java", "Static", True, 1995)
print(java)

languages = [python, ruby, visual_basic, java]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
