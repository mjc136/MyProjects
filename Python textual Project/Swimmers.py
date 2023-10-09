import os
import webbrowser
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import *
from textual.events import *
from textual.widgets.option_list import *

from swim_utils import *; #created by Paul Barry
from hfpy_utils import *; #created by Paul Barry
from my_utils import *

FOLDER = r"C:\Users\mjcul\OneDrive - Institute of Technology Carlow\Year 3\Cloud Dev\CA\swimdata"

NAMES = getNames(FOLDER) # from my_utils.py
SORTED_NAMES = sorted(NAMES) # 
 
class SwimmerApp(App):
    """Main application."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Select([(name, name) for name in SORTED_NAMES])
        yield Footer()
            
    CSS_PATH = "Swimmers.tcss"

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    @on(Select.Changed) # when name is chosen
    def select_changed(self, event: Select.Changed) -> None:
        if event.value is not None:
            """Handle the select changed event."""
            self.title = str(event.value)
            self.swimmer_name = event.value
            self.mount(Label(str("Swimmer '" + self.swimmer_name + "' has been selected.")))

            self.show_swimmer_events(self.swimmer_name)        

    def show_swimmer_events(self, swimmer_name):
        """Create option list for events."""
        swimmer_events_list = list_swimmer_events(FOLDER, swimmer_name)
        optionlist = OptionList()
        for i in range(len(swimmer_events_list)):
            optionlist.add_option(Option(str(swimmer_events_list[i])))
        self.mount(optionlist) 

       
    @on(OptionList.OptionSelected)  # when event is selected
    def select_event(self, event: OptionList.OptionSelected) -> None:
        swimmer_event = str(event.namespace)
        html_content = self.create_html(self.swimmer_name, swimmer_event)
        with open(self.swimmer_name + ".html", "w") as df:
            print(html_content, file=df)  
            webbrowser.open_new_tab(self.swimmer_name + ".html")

  
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark 


    def create_html(self) -> None:
        """Create the HTML file."""
        """inspired from BarChart.ipynb created by Paul Barry"""

        data = self.get_swimmer_data(self.swimmer_name)
        name, age, distance, stroke, times, values, average = data 
        title = f"{name} (Under {age}) {distance} - {stroke}"

        converts = []
        for n in values:
            converts.append(convert2range(n, 0, max(values)+50, 0, 400))

        times.reverse()
        converts.reverse()

        body = ""
        for t, c in zip(times, converts):
            svg = f""" 
                        <svg height="30" width="400">
                                <rect height="30" width="{c}" style="fill:rgb(0,0,255);" />
                        </svg>{t}<br />
                    """
            body = body + svg

        header = f"""
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>
                            {title}
                        </title>
                    </head>
                    <body>
                        <h3>{title}</h3>
                """

        footer = f""" 
                        <p>Average: {average}</p>
                    </body>
                </html>
                """
        
        html = header + body + footer
        return html
    

if __name__ == "__main__":
    app = SwimmerApp()
    app.run()