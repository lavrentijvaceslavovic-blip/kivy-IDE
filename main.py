import io
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MobileIDEApp(App):

  def build(self):
    # Главный контейнер (элементы вертикально друг под другом)
    layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

    # Метка для верхнего поля
    layout.add_widget(
        Label(
            text='Код для выполнения:',
            size_hint=(1, 0.05),
            halign='left',
            valign='middle',
        )
    )

    # Верхнее поле ввода кода
    self.code_input = TextInput(
        text=(
            'print("Привет с телефона через Kivy!")\nx = 10 + 32\nprint(f"Ответ:'
            ' {x}")'
        ),
        multiline=True,
        font_size=16,
        background_color=(0.15, 0.15, 0.15, 1),
        foreground_color=(1, 1, 1, 1),
    )
    layout.add_widget(self.code_input)

    # Кнопка запуска
    run_btn = Button(
        text='▶ Запустить код',
        size_hint=(1, 0.12),
        background_color=(0.2, 0.7, 0.3, 1),
    )
    run_btn.bind(on_press=self.execute_code)
    layout.add_widget(run_btn)

    # Метка для нижнего поля
    layout.add_widget(
        Label(
            text='Результат (консоль):',
            size_hint=(1, 0.05),
            halign='left',
            valign='middle',
        )
    )

    # Нижнее поле вывода (консоль)
    self.output_box = TextInput(
        text='Здесь появится результат...',
        readonly=True,
        multiline=True,
        font_size=14,
        background_color=(0.05, 0.05, 0.05, 1),
        foreground_color=(0, 1, 0, 1),  # Зеленый текст терминала
    )
    layout.add_widget(self.output_box)

    return layout

  def execute_code(self, instance):
    # Перенаправляем print() в текстовое поле
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
      user_code = self.code_input.text
      exec(user_code)
      result = new_stdout.getvalue()
      self.output_box.text = (
          result if result else 'Код выполнен без вывода (нет print).'
      )
    except Exception as e:
      self.output_box.text = f'Ошибка:\n{e}'
    finally:
      sys.stdout = old_stdout


if __name__ == '__main__':
  MobileIDEApp().run()