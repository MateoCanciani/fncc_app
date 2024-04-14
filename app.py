import re
from unidecode import unidecode
import dash
from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from script import check_answer

app = dash.Dash(external_stylesheets=[dbc.themes.LUX],
                suppress_callback_exceptions=True)


style = {
    "textAlign": "center",
    "padding": "30px",
} 

level_button_style = {"textAlign": "center", "margin":"30px","background-color": "#32327a"}

questions = {
    "A1": ("1Q01", "Q02", "Q03", "Q04", "Q05"),
    "A2": ("2Q01", "Q02", "Q03", "Q04", "Q05"),
    "B1": ("3Q01", "Q02", "Q03", "Q04", "Q05"),
    "B2": ("4Q01", "Q02", "Q03", "Q04", "Q05")
}

answers = {"A1": ("A01", "A02", "A03", "A04", "A05"),
           "A2": ("A01", "A02", "A03", "A04", "A05"),
           "B1": ("A01", "A02", "A03", "A04", "A05"),
           "B2": ("A01", "A02", "A03", "A04", "A05")}

links = {"A1":"http://1.com/",
        "A2": "http://2.com/",
        "B1": "http://3.com/",
        "B2": "http://4.com/"}

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
        dmc.Col(
            html.Div(
                dmc.Button("LET'S GET STARTED",id='start-button',size="xl",leftIcon=DashIconify(icon="formkit:submit", width=20,),variant="gradient",gradient={"from": "red", "to": "orange"},),style={"textAlign": "center","padding": "60px,0px,0px,0px"}
            )
        ), 
   
    ]#,
    #mb=100
)

levels = [["A1", "Beginner"], ["A2", "Medium"], ["B1", "Advanced"], ["B2", "Master"]]
level_selector_container = html.Div([
    dmc.Center([
        dmc.Grid(
            dmc.Col([
                dmc.Text("How would you define your French level so far ?",weight = 900, size ="30px"),
                dmc.RadioGroup(
                    [dmc.Radio(l, value=k,style={'margin': '0px 0px 0px 50px'}) for k, l in levels],
                    id="radiogroup-simple",
                    value="react",
                    label="Select your favorite framework/library",
                    size="sm",
                    mt=10,
                    style={"textAlign": "center"}),
                dmc.Button("CONFIRM", id='page2_button', size="xl", leftIcon=DashIconify(icon="formkit:submit", width=20,), variant="gradient", gradient={"from": "red", "to": "orange"}, style={"textAlign": "center", "padding": "60px,0px,0px,0px"})
            ])
        )
    ])
], style={'margin': '200px 0px 0px 0px'})


questions_container = dmc.Grid(
    [
        dmc.Col(
            [
                dmc.Text("question",id="question-box", weight = 700, size ="50px"),
                dmc.Center(
                    dmc.TextInput(label="Fill the blank in the sentence above :",id="answer-box",placeholder="Please type your answer here", style={"width": 400,"marginTop": "40px"},radius="md")
                            ), 
                dmc.Text("",id="user-answer-text"), 
                html.Div(
                    dmc.Button("Confirm answer",id='submit-answer-button',n_clicks=0,size="xl",leftIcon=DashIconify(icon="formkit:submit", width=20,),variant="gradient",gradient={"from": "red", "to": "orange"},),style={"textAlign": "center","padding": "0px,0px,0px,0px","marginTop": "80px"}),
                dmc.Text("",id='test')
            ] 
        ,style={"textAlign": "center", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}),     
    ]#,
    #mb=100
)

results_container = dmc.Grid(
    [
        dmc.Col(
            [
                dmc.Title('Nice job ! you finished the test ', className="animate__animated animate__fadeIn",order=1,align='center'),
                #dmc.Text(f'We estimated that your level was {level}',align='center',size="xl")                
            ],style={'padding': '40px 0px 0px 0px'}
        ),
        dmc.Col(
            html.Div(dmc.Center(dmc.Image(src='assets/logo.png', height="350px", width="350px")), style={"marginLeft": "110px"}),style={"padding":"30px"}
        ),
        dmc.Col(
            [
            dmc.Text(children=["You can now click ",dcc.Link("here", href=links[level],id="link")," to register for the French class best adapted to your level!"],align="center",size="xl",weight=700),
            dmc.Text("Thanks you for helping us to provide you the best.",align="center",size="xl",style={"padding":"20px 0px 0px 0px"})
            ]
        )        
    ]
)

app.layout = html.Div(
    [
        dmc.Header(height=20,
            fixed=True,
            children=[dmc.Text("")],
            style={"backgroundColor": "#f79f35"},
        ),
        dmc.Container(
            welcome_container,id="container")
        ,
        dmc.Footer(
            height=40,
            fixed=True,
            children=[dmc.Text("This test is not an official test. If you want to assess your French level in an official way, please get in touch with the FNCC",color="white",align="center")], #ADD STOP LOGOS SURROUNDING THE DISCLAIMER
            style={"backgroundColor": "#ee5b49"},
        ),
        dcc.Store(id="level", data=("")),
        dcc.Store(id="score",data=0)
   ] 
)

#Page 1 to page 2
@app.callback(
    Output("container", "children", allow_duplicate=True),
    Input("start-button", "n_clicks"),
    prevent_initial_call=True)


def update_first_page(n_clicks) :
    if n_clicks is None : 
        return welcome_container
    elif n_clicks >= 1 :
        return level_selector_container

#Page 2 level selector + transition to page 3
@app.callback(
    Output("container", "children", allow_duplicate=True),
    Output("level", "data"),
    Input("page2_button", "n_clicks"),
    State("radiogroup-simple", "value"),
    prevent_initial_call=True)


def update_second_page(n_clicks, choice):
    if n_clicks is None:
        return level_selector_container, ""
    elif n_clicks > 0 and choice in ["A1", "A2", "B1", "B2"]:
        return questions_container, choice
    elif n_clicks > 0 and not choice:
        return level_selector_container, ""  #Erreur de callback si l'utilisateur presse submit sans choisir de niveau

#Question refreshing 
@app.callback(
    Output('question-box',"children"),
    Input('submit-answer-button','n_clicks'),
    State('level','data')
    )


def update_questions(n_clicks,level) : #ajouter current level
    asked_question = questions[level][n_clicks]
    return asked_question

#Question checking + score adding
@app.callback(
    Output('score', 'data'),
    Input('submit-answer-button', 'n_clicks'),
    State('answer-box', 'value'),
    State('level', 'data'),
    State('score', 'data'))


def check_answer(n_clicks, answer, level, score):
    correct_answer = answers[level][n_clicks-1]
    ascii_user_answer = unidecode(answer.strip())
    if ascii_user_answer.lower() == correct_answer.lower():
        score += 1
        return score 
    else:
        return score

# Affichage du score sur la page
@app.callback(
    Output('test', 'children'),
    Input('score', 'data'))

def display_score(score):
    score = score
    return f"Current score: {score}"

if __name__ == "__main__":
    app.run_server(debug=True)