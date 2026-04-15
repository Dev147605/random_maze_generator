import panel as pn
import math
pn.extension()

select = pn.widgets.Select(name = "Select",options={"25":25,
                                                   "49":49,
                                                   "81":81,
                                                   "121":121})
button = pn.widgets.Button(name="Generate Maze")

def on_click(event):
    global numberSquare
    numberSquare = select.value
    print(f"Generating a maze with dimensions {int(math.sqrt(select.value))} x {int(math.sqrt(select.value))}")

button.on_click(on_click)

app = pn.Column(select,button)

app.servable()
pn.serve(app,show=True)