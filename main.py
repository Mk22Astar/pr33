from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation


class SimpleAnimationApp(App):
    def build(self):
        # Лейаут, занимающий весь экран
        layout = FloatLayout(size_hint=(1, 1))

        # Кнопка, по нажатию на которую начнется анимация
        button = Button(text='Запустить анимацию', size_hint=(None, None), size=(500, 100),
                        pos_hint={'center_x': 0.5, 'center_y': 0.1})
        button.bind(on_press=self.start_animation)
        layout.add_widget(button)

        # Объект, который будет анимироваться (картинка)
        self.animated_image = Image(source='mem.jpg', size_hint=(None, None), size=(200, 200),
                                    pos=(layout.width * 0.5 - 100, layout.height * 0.5 - 100))
        layout.add_widget(self.animated_image)

        # Переменная для хранения текущей анимации
        self.current_animation = None

        return layout

    def start_animation(self, instance):
        # Если существует текущая анимация, остановим её
        if self.current_animation:
            self.current_animation.stop(self.animated_image)

        # Обновляем позицию изображения для начала анимации
        self.animated_image.pos = (self.root.width * 0.5 - 100, self.root.height * 0.5 - 100)

        # Создаем анимацию для изменения позиции объекта в квадрате
        animation = Animation(pos=(self.root.width * 0.7 - 100, self.root.height * 0.7 - 100), duration=2)
        animation += Animation(pos=(self.root.width * 0.7 - 100, self.root.height * 0.3 - 100), duration=2)
        animation += Animation(pos=(self.root.width * 0.3 - 100, self.root.height * 0.3 - 100), duration=2)
        animation += Animation(pos=(self.root.width * 0.3 - 100, self.root.height * 0.7 - 100), duration=2)
        animation += Animation(pos=(self.root.width * 0.5 - 100, self.root.height * 0.5 - 100), duration=2)
        animation.repeat = True

        # Сохраняем текущую анимацию
        self.current_animation = animation

        # Запускаем анимацию для объекта
        animation.start(self.animated_image)


if __name__ == '__main__':
    SimpleAnimationApp().run()
