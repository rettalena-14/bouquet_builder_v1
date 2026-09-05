import dash
from dash import dcc, html, Input, Output

# -----------------------------
# COLOR DATA
# -----------------------------

color_hex = {
    "red": "#e63946",
    "crimson": "#a4161a",
    "maroon": "#800000",
    "pink": "#f699cd",
    "hot pink": "#ff1694",
    "light pink": "#FEC5E5",
    "orange": "#ff7f11",
    "coral": "#ff6f61",
    "peach": "#ffdab9",
    "yellow": "#ffd60a",
    "light yellow": "#fff3b0",
    "blue": "#0077b6",
    "navy": "#03045e",
    "light blue": "#90e0ef",
    "green": "#2d6a4f",
    "sage": "#9caf88",
    "white": "#ffffff",
    "cream": "#fff1e6",
    "brown": "#7f5539",
    "beige": "#eae0d5",
    "black": "#000000"
}

color_groups = {
    "red": ["red", "crimson"],
    "maroon": ["maroon"],
    "pink": ["pink", "hot pink"],
    "light_pink": ["light pink"],
    "orange": ["orange", "coral", "peach"],
    "yellow": ["yellow", "light yellow"],
    "blue": ["blue", "navy"],
    "light_blue": ["light blue"],
    "green": ["sage"],
    "greens": ["green", "sage"],
    "white": ["white", "cream"],
    "brown": ["brown", "beige"],
    "black": ["black"]
}

color_modes = {
    "monochromatic": "dynamic",
    "wicked": ["pink", "green"],
    "gender_reveal": ["pink", "blue"],
    "spring": ["yellow", "light_pink", "light_blue", "green"],
    "chic_maroon": ["maroon", "green"],
    "greeneries": ["greens", "white"],
    "summer": ["yellow", "pink", "light_blue", "green", "orange"],
    "dark_romance": ["red", "black", "maroon"],
    "neutrals": ["brown", "white"]
}

# -----------------------------
# FLOWER DATA
# -----------------------------

flower_roles = {
    "roses": {
        "secondary": ["lisianthus", "carnations"],
        "filler": ["asters", "carnation spray", "baby's breath"],
        "line": ["calla lilies"]
    },
    "peonies": {
        "secondary": ["lisianthus", "carnations"],
        "filler": ["wax flowers", "viburnum"],
        "line": ["calla lilies"]
    },
    "tulips": {
        "secondary": ["lisianthus", "carnation"],
        "filler": ["chamomile", "viburnum"],
        "line": ["ecalyptus", "oncidium orchids"]
    },
    "sunflowers": {
        "secondary": ["carnations"],
        "filler": ["baby's breath", "queen anne's lace"],
        "line": ["ecalyptus", "oncidium orchids"]
    },
    "anthuriums": {
        "secondary": ["lisianthus", "carnations"],
        "filler": ["queen anne's lace"],
        "line": ["delphinium"]
    }
}

flower_color_options = {
    "roses": ["pink", "light pink", "white", "peach", "red", "crimson", "hot pink", "beige", "blue", "sage", "coral", "yellow", "black"],
    "tulips": ["pink", "light pink", "white", "peach", "red", "beige", "blue", "coral", "yellow", ],
    "peonies": ["pink", "white", "red", "coral", "yellow", "maroon"],
    "sunflowers": ["yellow"],
    "anthuriums": ["pink", "white", "green", "orange", "brown", "black","red"]
}

flower_images = {
    "roses": "https://images.unsplash.com/photo-1559563362-c667ba5f5480?q=80&w=1001&auto=format&fit=crop",
    "lisianthus": "https://images.unsplash.com/photo-1705818631170-c93e1955ad61?q=80&w=987&auto=format&fit=crop",
    "carnations": "https://plus.unsplash.com/premium_photo-1677178629088-ba7d3a23049a?q=80&w=987&auto=format&fit=crop",
    "aster": "https://images.unsplash.com/photo-1711911944478-a4bec4c536e8?q=80&w=1035&auto=format&fit=crop",
    "carnation spray": "https://images.unsplash.com/photo-1675687106027-13a77f057716?q=80&w=1770&auto=format&fit=crop",
    "baby's breath": "https://images.unsplash.com/photo-1608153917926-c467b4e23b6f?q=80&w=3087&auto=format&fit=crop",
    "calla lilies": "https://images.unsplash.com/photo-1625068786411-4e7fe1f6191c?q=80&w=3270&auto=format&fit=crop",
    "peonies": "https://unsplash.com/photos/pink-and-white-flower-in-tilt-shift-lens-uXouToDHxPU",
    "anthuriums": "https://images.unsplash.com/photo-1594076353236-85d8e500be80?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "tulips": "https://images.unsplash.com/photo-1614791199038-6869a104fe5f?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "sunflowers": "https://plus.unsplash.com/premium_photo-1676692121474-a3e3890d39f4?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "queen anne's lace": "https://plus.unsplash.com/premium_photo-1677329951281-63bac31a9a49?q=80&w=982&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "chamomile": "https://images.unsplash.com/photo-1640918440379-82c68390ea5b?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "oncidium orchids": "https://images.unsplash.com/photo-1679966519593-43d645c9c433?q=80&w=1674&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "delphinium": "https://images.unsplash.com/photo-1567061426127-c16e990ee5ef?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "wax flowers": "https://images.unsplash.com/photo-1773871784019-07c74b74e0b5?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "viburnum": "https://images.unsplash.com/photo-1777451650911-3ec420ba9701?q=80&w=1674&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "ecalyptus": "https://plus.unsplash.com/premium_photo-1744743523609-5563bfab1cf7?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
}

# -----------------------------
# COLOR LOGIC
# -----------------------------

def get_allowed_colors(mode, base_color=None):
    if mode == "monochromatic":
        if base_color is None:
            return []
        return color_groups.get(base_color, [])

    palette = color_modes.get(mode, [])

    base_group = None
    if base_color is not None:
        for group, shades in color_groups.items():
            if base_color in shades:
                base_group = group
                break

        if base_group not in palette:
            return []

    expanded = []
    for group in palette:
        expanded.extend(color_groups.get(group, []))

    return expanded


def get_valid_modes(base_color):
    valid_modes = []

    for mode, palette in color_modes.items():
        if mode == "monochromatic":
            valid_modes.append(mode)
            continue

        for group, shades in color_groups.items():
            if base_color in shades and group in palette:
                valid_modes.append(mode)

    return valid_modes


# -----------------------------
# DASH APP
# -----------------------------

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("🌸 Flower Color & Bouquet Builder"),

    html.Div([

        # LEFT SIDE (COLOR)
        html.Div([
            html.H2("🎨 Color Selection"),

            html.Label("Select Base Color"),
            dcc.Dropdown(id="color-dropdown"),

            html.Br(),

            html.Label("Select Mode"),
            dcc.Dropdown(id="mode-dropdown"),

            html.Br(),

            html.Div(id="color-output")

        ], style={"width": "48%", "display": "inline-block", "verticalAlign": "top"}),

        # RIGHT SIDE (FLOWER)
        html.Div([
            html.H2("🌹 Flower Builder"),

            html.Label("Select Focal Flower"),
            dcc.Dropdown(
                id="focal-flower-dropdown",
                placeholder="Choose a focal flower"
            ),

            html.Br(),

            html.Div(id="flower-output")

        ], style={"width": "48%", "display": "inline-block", "verticalAlign": "top"})

    ])
])


# -----------------------------
# CALLBACKS
# -----------------------------

# Color depends on Flower
@app.callback(
    Output("color-dropdown", "options"),
    Input("focal-flower-dropdown", "value")
)
def update_color_options(focal):
    if not focal:
        all_colors = [c for group in color_groups.values() for c in group]
        return [{"label": c, "value": c} for c in all_colors]

    allowed = flower_color_options.get(focal, [])
    return [{"label": c, "value": c} for c in allowed]


# Flower depends on Color
@app.callback(
    Output("focal-flower-dropdown", "options"),
    Input("color-dropdown", "value")
)
def update_flower_options(selected_color):
    all_flowers = list(flower_roles.keys())

    if not selected_color:
        return [{"label": f.capitalize(), "value": f} for f in all_flowers]

    valid_flowers = [
        f for f, colors in flower_color_options.items()
        if selected_color in colors
    ]

    return [{"label": f.capitalize(), "value": f} for f in valid_flowers]


@app.callback(
    Output("mode-dropdown", "options"),
    Input("color-dropdown", "value")
)
def update_modes(base_color):
    if not base_color:
        return []

    modes = get_valid_modes(base_color)
    return [{"label": m, "value": m} for m in modes]


@app.callback(
    Output("color-output", "children"),
    Input("color-dropdown", "value"),
    Input("mode-dropdown", "value")
)
def show_color_results(base_color, mode):
    if not base_color or not mode:
        return "Select options to see color recommendations"

    colors = get_allowed_colors(mode, base_color)

    return html.Div([
        html.H3("Recommended Colors:"),
        html.Div([
            html.Div([
                html.Div(
                    style={
                        "backgroundColor": color_hex.get(c, "#ccc"),
                        "width": "60px",
                        "height": "60px",
                        "borderRadius": "8px",
                        "border": "1px solid #ccc"
                    }
                ),
                html.P(c)
            ], style={"display": "inline-block", "margin": "10px"})
            for c in colors
        ])
    ])


@app.callback(
    Output("flower-output", "children"),
    Input("focal-flower-dropdown", "value")
)
def update_flower_recommendations(focal):
    if not focal:
        return "Select a focal flower"

    data = flower_roles.get(focal, {})

    def render_section(title, flowers):
        return html.Div([
            html.H4(title),
            html.Div([
                html.Div([
                    html.Img(
                        src=flower_images.get(f, ""),
                        style={"width": "100px", "height": "100px"}
                    ),
                    html.P(f)
                ], style={"display": "inline-block", "margin": "10px"})
                for f in flowers
            ])
        ])
    
    return html.Div([
        render_section("🌸 Secondary Flowers", data.get("secondary", [])),
        render_section("🌿 Fillers", data.get("filler", [])),
        render_section("🌱 Line Flowers", data.get("line", []))
    ])




# -----------------------------
# RUN
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)