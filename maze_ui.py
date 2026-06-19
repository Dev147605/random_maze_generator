import panel as pn
import math
import random_maze_generator
import matplotlib.pyplot as plt
pn.extension('matplotlib')

select = pn.widgets.Select(name = "Select",options={"5 x 5":25,
                                                   "7 x 7":49,
                                                   "9 x 9":81,
                                                   "11 x 11":121,
                                                   "13 x 13":169})
button = pn.widgets.Button(name="Generate Maze")
maze_display = pn.pane.Matplotlib(width=500, height=500, tight=True)
def on_click(event):
    global numberSquare
    numberSquare = select.value
    print(f"Generating a maze with dimensions {int(math.sqrt(select.value))} x {int(math.sqrt(select.value))}")
    fig = random_maze_generator.initalize_maze(numberSquare)
    maze_display.object = fig
    maze_display.param.trigger('object')
    plt.close(fig)
button.on_click(on_click)

app = pn.Column(pn.pane.Markdown("## Maze Generator"),
                select,
                button,
                maze_display)

app.servable()
pn.serve(app,show=True)