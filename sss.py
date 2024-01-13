from kivy.app import App
from kivy.uix.image import AsyncImage

class GifApp(App):
    def build(self):
        # Установка GIF-анимации с помощью AsyncImage
        gif_image = AsyncImage(source='path/to/your/animation.gif')
        return gif_image

if name == 'main':
    GifApp().run()
