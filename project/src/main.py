# Основная логика
from src.parser import KnowledgeBase
from src.prompts import build_prompt

class HypothesisGenerator:
    def __init__(self):
        self.kb = KnowledgeBase()
    
    def generate(self, problem, constraints):
        context = self.kb.search(problem)
        prompt = build_prompt(problem, constraints, context)
        # Здесь будет вызов Yandex AI Studio
        return {"status": "Генерация гипотез", "problem": problem}
