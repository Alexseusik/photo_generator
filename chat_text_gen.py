import subprocess
from openai import OpenAI
from datetime import datetime

today_date = datetime.now().strftime('%d.%m.%Y')

part1 = "sk-proj-bY2mudDeG2ZSTnBK6jn4bMfH-K6pCiA8hlazQaqX_"
part2 = "9P5rnbDitIKWK8BiG5mW-5z6Ews8m3hljT3BlbkFJx7mhxQOxJFbu2p-nASlKt4u"
part3 = "SjNJVovVq08TEQl9h4FzF7B1h497INjw6r3wTCZxmkUWW7K1IQA"

api_key = part1+part2+part3

subprocess.run(['export', f'OPENAI_API_KEY="{api_key}"'], shell=True)

client = OpenAI(api_key=part1+part2+part3)


def create_text():
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": f"Існує канал ліцензованої мережі обмінних пунктів валют Монета. Щоденно я вітаю підписників каналу приблизно наступним постом: \n\nДоброго ранку, друзі! 12 квітня 2024 року нагадує нам про важливість мрій та непереможного духу. \"Мрії можуть стати реальністю, якщо ми маємо відвагу їх переслідувати,\" – сказав Волт Дісней. Це день, щоб замислитися над власними мріями та зробити кроки на їхню зустріч, незалежно від обставин. У МОНЕТА ми цінуємо кожного, хто не боїться мріяти велико та докладає зусиль для їхнього здійснення. Наші обмінні пункти готові надати вам підтримку та вигідні курси, аби кожна ваша фінансова операція була кроком до реалізації ваших амбіцій. Бажаємо вам дня, наповненого вірою у власні сили та переконанням у тому, що перед вами відкриті всі двері. Нехай ваші мрії ведуть вас через виклики до нових вершин. З найкращими побажаннями, ваша команда МОНЕТА. \n\nДавай продовжимо цю цікаву традицію. Запропонуй піст на {today_date}."
            }
          ]
        },
        {
          "role": "assistant",
          "content": [
            {
              "type": "text",
              "text": "Доброго ранку, друзі! 24 вересня 2024 року – це чудовий момент для роздумів та саморозвитку. Сьогодні хочемо нагадати вам про важливість не зупинятися на досягнутому і завжди шукати нові можливості для вдосконалення. \"Ваша справжня сила полягає в тому, щоб ніколи не втрачати надію,\" – стверджує відома мудрість.\n\nЦей день може стати ідеальною нагодою для аналізу вашого фінансового стану, планування нових цілей і втілення мрій у реальність. У МОНЕТА ми завжди готові вас підтримати в усіх ваших починаннях, пропонуючи вигідні курси обміну та консультації, які допоможуть вам здійснити ваші фінансові плани.\n\nБажаємо вам продуктивного дня, наповненого новими ідеями і рішучістю. Нехай ваші зусилля приводять до успіху, а мрії надихають вас на великі досягнення. Ваші мрії – це ваш потенціал! З найкращими побажаннями, ваша команда МОНЕТА."
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
