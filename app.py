import dash
from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

style = {
    "textAlign": "center",
    "padding": "30px",
} 

level_button_style = {"textAlign": "center", "margin":"30px","background-color": "#32327a"}

welcome_container = dmc.Grid(
    [
        dmc.Col(
            [
                dmc.Title('Welcome to the FNCC french test !', id='page1-title', className="animate__animated animate__fadeIn",order=1,align='center'),
                dmc.Text("You will soon start taking FNCC french courses ?" ,align='center',size="xl"),
                dmc.Text("This test is made for you : with a quick assesment of your french language skills you will be able to know which course fits you the best !" ,align='center',size="xl"),
                html.Div(dmc.Center(dmc.Image(src='assets/logo.png', height="300px", width="300px")), style={"marginLeft": "110px"})
            ] 
        ,style=style),
        dmc.Container([
            dmc.Button('Beginner', id='button-1',color="#32327a",style=level_button_style),
            dmc.Button('Medium', id='button-2',style=level_button_style),
            dmc.Button('Advanced', id='button-3',style=level_button_style),
            dmc.Button('Expert', id='button-4',style=level_button_style)], 
            ), 
        dmc.Col(
            html.Div(
                dmc.Button("LET'S GET STARTED",id='start-button',size="xl",leftIcon=DashIconify(icon="formkit:submit", width=20,),variant="gradient",gradient={"from": "red", "to": "orange"},),style={"textAlign": "center","padding": "60px,0px,0px,0px"}
            )
        ), 
   
    ]#,
    #mb=100
)

questions_container = dmc.Grid(
    [
        dmc.Col(
            [
                dmc.Text("question",id="question", weight = 700, size ="50px"),
                dmc.Center(
                    dmc.TextInput(label="Fill the blank in the sentence above :",id="answer-box",placeholder="Please type your answer here", style={"width": 400,"marginTop": "40px"},radius="md")
                            ), 
                dmc.Text("",id="user-answer-text"), 
                html.Div(
                    dmc.Button("Confirm answer",id='submit-answer-button',size="xl",leftIcon=DashIconify(icon="formkit:submit", width=20,),variant="gradient",gradient={"from": "red", "to": "orange"},),style={"textAlign": "center","padding": "0px,0px,0px,0px","marginTop": "80px"}
                        )
            ] 
        ,style={"textAlign": "center", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}),     
    ]#,
    #mb=100
)

results_container = dmc.Text("results")

app.layout = html.Div(
    [
        dmc.Header(height=20,
            fixed=True,
            children=[dmc.Text("")],
            style={"backgroundColor": "#f79f35"},
        ),
        dmc.Container(
            welcome_container,id="container"
        ),
        dmc.Footer(
            height=40,
            fixed=True,
            children=[dmc.Text("This test is not an official test. If you want to assess your French level in an official way, please get in touch with the FNCC",color="white",align="center")], #ADD STOP LOGOS SURROUNDING THE DISCLAIMER
            style={"backgroundColor": "#ee5b49"},
        )
   ] 
)

@app.callback(
            Output("container","children"),
            Input("start-button","n_clicks")              
)


def update_container(n_clicks) :
    if n_clicks is None : 
        return welcome_container
    elif n_clicks >= 1 :
        return questions_container
    
if __name__ == "__main__":
    app.run_server(debug=True)
