# Промпты для LLM
def build_prompt(problem, constraints, context):
    prompt = f"""
Ты эксперт-металлург с 20-летним опытом.
Задача: {problem}
Ограничения: {constraints}
Найденные данные: {context}

Сгенерируй 5 гипотез для решения задачи.
Для каждой гипотезы укажи:
1. action - что сделать
2. mechanism - почему это сработает
3. novelty - новизна
4. risks - риски
5. expected_effect - ожидаемый эффект
6. references - ссылки на источники

Ответ дай в формате JSON.
"""
    return prompt
