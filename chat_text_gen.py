from openai import OpenAI
from datetime import datetime

today_date = datetime.now().strftime('%d.%m.%Y')

client = OpenAI()


def create_text():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "text": "Ти найкращий асистент для роботи і завжди правильно видаєш відповідь. Пиши лише основний текст, не пиши ніякого додаткового тексту",
                        "type": "text"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Існує канал ліцензованої мережі обмінних пунктів валют Монета. Щоденно я вітаю підписників каналу приблизно наступним постом: \n\nДоброго ранку, друзі!\n\nСьогодні, 25 вересня 2024 року, я хочу нагадати, що \"Віра в себе — це основа успіху.\" Не бійтеся довіряти своїм можливостям і приймати нові виклики.\n\nЗапрошую вас завітати до нас у МОНЕТА, де ми завжди раді бачити вас і готові допомогти з вашими фінансовими питаннями.\n\nБажаю нам усім дня, сповненого віри в себе і свої сили. Нехай цей день наблизить нас до наших мрій.\n\nЗ повагою, ваша команда МОНЕТА.\n\nДавай продовжимо цю цікаву традицію. Запропонуй піст на {today_date}."
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )

    return response.choices[0].message.content
