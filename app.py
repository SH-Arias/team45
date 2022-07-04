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
dash_app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY])



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
dash_app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)


# This call will be used with Gunicorn server
server = dash_app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    dash_app.run_server(debug=True, host='0.0.0.0', port='80')
