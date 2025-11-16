"""CP1404 - Dynamic Labels"""

import os

os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that creates a Label for each name."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Peter Thamu", "Rachel Thamu", "Christine Thamu", "Sylvia Thamu"]

    def build(self):
        """Build the GUI and create the labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")

        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

        return self.root


DynamicLabelsApp().run()
