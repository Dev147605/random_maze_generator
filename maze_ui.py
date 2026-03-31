import panel as pn
import math
pn.extension()

select = pn.widgets.Select(name = "Select",options={"25":25,
                                                   "36":36,
                                                   "49":49,
                                                   "64":64,
                                                   "81":82,
                                                   "100":100})
button = pn.widgets.Button(name="Generate Maze")
def on_click(event):
    print(f"Generating a maze with size {int(math.sqrt(select.value))} x {int(math.sqrt(select.value))}")

button.on_click(on_click)

app = pn.Column(select,button)

app.servable()
pn.serve(app,show=True)