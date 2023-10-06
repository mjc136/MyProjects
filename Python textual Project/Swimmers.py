import os
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import *
from textual.events import *
from textual.widgets.option_list import *
#from textual.screen import Screen

from swim_utils import *
from my_utils import *

FOLDER = r"C:\Users\mjcul\OneDrive - Institute of Technology Carlow\Year 3\Cloud Dev\CA3\swimdata"

NAMES = getNames(FOLDER)
SORTED_NAMES = sorted(NAMES)


class SwimmerApp(App):
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Select([(name, name) for name in SORTED_NAMES])
        yield Footer()

            
    CSS_PATH = "Swimmers.tcss"

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        """Handle the select changed event."""
        self.title = str(event.value)
        swimmer_name = event.value
        self.mount(Label(str("Swimmer '" + swimmer_name + "' has been selected.")))

        self.show_swimmer_events(swimmer_name)

    def show_swimmer_events(self, swimmer_name):
        """Create option list for events."""
        swimmer_events_list = list_swimmer_events(FOLDER, swimmer_name)
        optionlist = OptionList()
        for i in range(len(swimmer_events_list)):
            optionlist.add_option(Option(str(swimmer_events_list[i])))
        self.mount(optionlist) 

        
    @on(OptionList.OptionSelected)
    def select_event(self,) -> None:
        self.mount(Label(str("Poo")))
 

        

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark 

if __name__ == "__main__":
    app = SwimmerApp()
    app.run()