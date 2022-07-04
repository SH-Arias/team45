#libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import os
#from callbacks import register_callbacks


request_path_prefix = None

#only for workspace in DS4A
#workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
#if workspace_user:
#    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

    
# Dash instance declaration
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY])

IMAGES_BASE_URL = 'https://storage.googleapis.com/lidar-data-01/images/'

list_of_images = [
    'section1','section2','section3','section4',
    'section5','section6','section7','section8',
    'section9','section10','section11'
    ]


#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([

    dbc.NavItem(dbc.NavLink( "Inicio", href="/")),
    dbc.DropdownMenu(
        [
            
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="Data Science",
    ),
    dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
    ],
    brand="DS4A Project",
    color="primary",
    dark=True,
    className="mb-2",
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)
@app.callback(
    dash.dependencies.Output('image', 'src'),
    [dash.dependencies.Input('image-dropdown', 'value')])

def update_image_src(value):
    return IMAGES_BASE_URL + value + '.png'

# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, debug=True)
