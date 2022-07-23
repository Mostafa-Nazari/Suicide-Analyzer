import plotly.express as plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas
import numpy
import dash


print("Hi")
# style tabs
tabs_styles = {
    'width': '50px',
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'fontFamily': 'cursive',
    'fontSize': '30px',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    'fontFamily': 'cursive',
    'fontSize': '30px',
}

# ----------------------------------------------------------#
# load dataframe

df = pandas.read_csv('dataset.csv')

# ----------------------------------------------------------#
# country list
country_name = numpy.unique(df['Country'])
country_list = [{'label': i, 'value': i} for i in country_name]
# ----------------------------------------------------------#
# wordwide line plot
word_line_df = df.groupby(['Year'],as_index = False).mean()
word_line_year = word_line_df['Year']
word_line_suicide = word_line_df['Suicides_100k_Pop']
 
word_line_plot = plotly.line(
    x = word_line_year,
    y = word_line_suicide,
    template= 'plotly_dark'
)

word_line_plot.update_traces(
    hovertemplate = "Suicide Number = %{y} <br> Year = %{x}"
)

word_line_plot.update_layout(
    title_text = "Average suicide per 100k population",
    title_font_size = 18,
    title_font_color = 'white',
    title_x = 0.5,
    title_y = 0.95,
    title_xanchor = "center",
    title_yanchor = 'top',
    margin_l = 100,
    xaxis_title = 'Years',
    xaxis_titlefont_size = 16,
    xaxis_title_standoff = 50,
    yaxis_title = 'Suicide  per  100  Pop',
    yaxis_titlefont_size = 16,
    yaxis_title_standoff = 30,

)
# ------------------------------------------------------------ #
# wordwide line plot by gender
word_line_sex_df = df.groupby(['Year', 'Sex'], as_index= False).mean()

word_line_sex_plot = plotly.line(
    word_line_sex_df,
    x='Year',
    y='Suicides_100k_Pop',
    color = 'Sex',
    template='plotly_dark'
)

word_line_sex_plot.update_traces(
    hovertemplate="Suicide Number = %{y} <br> Year = %{x}"
)

word_line_sex_plot.update_layout(
    title_text="Average suicide per 100k population by gender",
    title_font_size=18,
    title_font_color='white',
    title_x=0.5,
    title_y=0.95,
    title_xanchor="center",
    title_yanchor='top',
    margin_l=100,
    xaxis_title='Years',
    xaxis_titlefont_size=16,
    xaxis_title_standoff=50,
    yaxis_title='Suicide  per  100  Pop',
    yaxis_titlefont_size=16,
    yaxis_title_standoff=30,

)
# ------------------------------------------------------------#
# wordwide pie chart by gender
word_pie_sex_df = df.groupby(['Sex'],as_index = False).sum()

word_pie_sex_plot = plotly.pie(word_pie_sex_df,
                               values = 'Suicide',
                               names = 'Sex',
                               template='plotly_dark',
                               title='Wordwide Suicide by gender')

word_pie_sex_plot.update_traces(textposition='inside', textinfo='percent+label',textfont_size = 16)

# ------------------------------------------------------------ #
# wordwide line plot by age
word_line_age_df = df.groupby(['Year', 'Age'], as_index= False).mean()

word_line_age_plot = plotly.line(
    word_line_age_df,
    x='Year',
    y='Suicides_100k_Pop',
    color = 'Age',
    template='plotly_dark'
)

word_line_age_plot.update_traces(
    hovertemplate="Suicide Number = %{y} <br> Year = %{x}"
)

word_line_age_plot.update_layout(
    title_text="Average suicide per 100k population by age",
    title_font_size=18,
    title_font_color='white',
    title_x=0.5,
    title_y=0.95,
    title_xanchor="center",
    title_yanchor='top',
    margin_l=100,
    xaxis_title='Years',
    xaxis_titlefont_size=16,
    xaxis_title_standoff=50,
    yaxis_title='Suicide  per  100  Pop',
    yaxis_titlefont_size=16,
    yaxis_title_standoff=30,

)
# ------------------------------------------------------------- #
# wordwide pie chart by age
word_pie_age_df = df.groupby(['Age'],as_index = False).sum()

word_pie_age_plot = plotly.pie(
    word_pie_age_df,
    values = 'Suicide',
    names = 'Age',
    template='plotly_dark',
    title='Wordwide Suicide by age'
)

word_pie_age_plot.update_traces(textposition='inside', textinfo='percent+label',textfont_size = 11)
# ------------------------------------------------------------- #
# Country Bar Chart
country_bar_chart_df = (df.groupby(['Country'], as_index=False).mean()).sort_values(by='Suicides_100k_Pop')
country_bar_chart_df = country_bar_chart_df.round()

country_bar_chart = plotly.bar(
            country_bar_chart_df,
            x='Suicides_100k_Pop',
            y='Country',
            orientation='h',
            text='Suicides_100k_Pop',
            template='plotly_dark'
        )
# -------------------------------------------------------------- #

FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"

app  = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG,FA])
server = app.server

app.layout = html.Div([
    
    html.Div([
        
        dbc.Navbar([
            
              dbc.Col(html.Img(src = "/assets/11.png", style = {'width':150,'height':50},id = 'navbar-image'),width=3),
              dbc.Col('Analyzing Suicide Rates (1985 to 2016 )', id = 'navbar-text', width={"size": 7, "offset": -2},
                      style = {'text-align':'center','color':'white', 'font-weight':'bold','font-family':'Cursive'})
           
        ],color = '#26272b')
    ]),
    
    html.Br(),
    html.Hr(),
    
    dbc.Col([  

                     html.P("Suicide is the act of intentionally causing one's own death. Mental disorders—including "
                     "depression, bipolar disorder, autism, schizophrenia, personality disorders, anxiety disor"
                     "ders, physical disorders such as chronic fatigue syndrome, and substance abuse—including "
                     "alcoholism and the use of benzodiazepines—are  risk factors.Some suicides are impulsive acts"
                     "due to stress, such as from financial difficulties, relationship problems such as breakups,"
                     "or bullying. Those who have previously attempted suicide are at a higher risk for future "
                     "attempts.Effective suicide prevention efforts include limiting access to methods of suicide—such"
                     "as firearms, drugs, and poisons; treating mental disorders and substance misuse; careful media" 
                     "reporting about suicide; and improving economic conditions. Even though crisis hotlines are "
                     "common, they have not been well studied."),
                     html.Br(),
                     html.Br(),
                     html.Br(),
                     html.P("Approximately 1.5% of people die by suicide. In a given year this is roughly 12 per 100,000 "
                    "people. Rates of completed suicides are generally higher among men than among women, ranging "
                    "from 1.5 times as much in the developing world to 3.5 times in the developed world. Suicide "
                    "is generally most common among those over the age of 70; however, in certain countries, those "
                    "aged between 15 and 30 are at the highest risk. There are an estimated 10 to 20 million non-fatal "
                    "attempted suicides every year. Non-fatal suicide attempts may lead to injury and long-term disabilities. "
                    "In the Western world, attempts are more common among young people and among females."),


    ],
    className = 'image-text'),

    html.Br(),
    html.Br(),
    html.Hr(),
    
    html.Div([

        dcc.Tabs(
            id="tabs",
            value='tab-1',
            children=[
                dcc.Tab(
                    label='Wordwide',
                    value='tab-1',
                    style=tab_style,
                    selected_style=tab_selected_style,
                    children= [

                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),

                        html.Div([
                                dbc.Row([
                                    dbc.Col([dcc.Graph(id='word-line', figure = word_line_plot)],width = {'size': 8, 'offset':2})
                                ]),

                                html.Br(),
                                html.Br(),
                                html.Hr(),

                                dbc.Row([
                                        dbc.Col([dcc.Graph(id = 'word-line-sex', figure = word_line_sex_plot)], lg=7, md=7, sm=12, xs=12),
                                        dbc.Col([dcc.Graph(id = 'word-pie-sex', figure = word_pie_sex_plot)], lg=5, md=5, sm=12, xs=12),
                                ]),

                                html.Br(),
                                html.Br(),
                                html.Hr(),

                                dbc.Row([
                                        dbc.Col([dcc.Graph(id='word-line-age', figure = word_line_age_plot)], lg=7, md=7, sm=12, xs=12),
                                        dbc.Col([dcc.Graph(id='word-pie-age', figure = word_pie_age_plot)],lg=5, md=5, sm=12, xs=12 ),
                                ]),
                        ])

                    ]),


                dcc.Tab(
                    id = 'tab-2',
                    label='Country',
                    value='tab-2',
                    style = tab_style,
                    selected_style = tab_selected_style,
                    children= [

                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),

                        html.Div([
                            dbc.Col([
                                dbc.Card([

                                    dbc.CardHeader('Filter',style={'font-size':25, 'font-weight':'bold'}),
                                    dbc.CardBody([
                                        dbc.Row([
                                            dbc.Col([
                                                html.Label('Select Countries',
                                                           className='font-weight-bold font-italic'),
                                                dcc.Dropdown(id = 'country-list',
                                                             options=country_list,
                                                             value='Albania',
                                                             clearable=True,
                                                             style={'color': 'black'})
                                            ],lg=6, md=6, sm=12, xs=12),

                                            dbc.Col([
                                                html.Label('Exclude Specific Date',
                                                           className='label-range font-weight-bold font-italic'),
                                                dcc.RangeSlider(
                                                    id='range-year',
                                                    min=1985,
                                                    max=2015,
                                                    value=[1985, 2015],
                                                    marks={
                                                        1985: '1985',
                                                        1990: '1990',
                                                        1995: '1995',
                                                        2000: '2000',
                                                        2005: '2005',
                                                        2010: '2010',
                                                        2015: '2015',
                                                    },

                                                )
                                            ],className='offset-lg-1  offset-md-1', lg=5, md=5, sm=12, xs=12),
                                        ])

                                    ])
                                ], style={'height':300})
                            ], lg=12, md=12, sm=12, xs=12)
                        ]),

                        html.Br(),
                        html.Br(),
                        html.Br(),

                        html.Div([

                            dbc.Row([

                                dbc.Col([
                                    dbc.Row(dbc.Col([dcc.Graph(id='country-bar')]),style={'height': '600px', 'overflow-y': 'scroll'}),
                                    dbc.Row(dbc.Col([dcc.Graph(id='country-pie-sex')]), style={'margin-top': '30px'}),
                                    dbc.Row(dbc.Col([dcc.Graph(id='country-pie-age')]), style={'margin-top': '30px'}),
                                ], lg=5, md=5, sm=12, xs=12 ),

                                dbc.Col([
                                    dbc.Row(dbc.Col([dcc.Graph(id='country-line')])),
                                    dbc.Row([dbc.Col([dcc.Graph(id='country-line-sex')])],style={'margin-top': '20px'}),
                                    dbc.Row([dbc.Col([dcc.Graph(id='country-line-age')])],style={'margin-top': '20px'}),
                                ], lg=7, md=7, sm=12, xs=12 )

                            ])
                        ])

                ])

            ]),

    ]),

    html.Div(
        [
           html.Div([

                    html.H5('About App',style = {'text-align':'center', 'font-weight':'bold','font-family':'Cursive'}),
                    html.Br(),
                    html.P("This app created with Dash Plotly. Dash is the most downloaded, "
                           "trusted Python framework for building ML & data science web apps."
                            "Built on top of Plotly.js, React and Flask, Dash ties modern UI elements" 
                            " like dropdowns, sliders, and graphs directly to your analytical Python code.",
                           style = {'text-align':'center', 'font-weight':'bold','font-family':'sans-serif'}),
            ]),

            html.Br(),
            html.Hr(),

            html.Div([
                    html.Br(),
                    html.I('  09337167395  ',className="fas fa-phone-square fa-1x mr-4 center"),
                    html.Br(),
                    html.I('  msnaa1392@gmail.com  ',className="fas fa-envelope fa-1x mr-4 center"),
            ], style = {'text-align':'center'}),


       ],
       className = 'footer',
    )

    
],
style = {'margin':30})


@app.callback(Output('country-bar','figure'),
              Input('tabs','value'))
def update_bar_chart(tab):
    if tab == 'tab-2':
        country_bar_chart.update_traces(
            textposition='outside',
            marker_color='blue',
            marker_line_color='black',
            marker_line_width=1,
            width=1,

        )

        country_bar_chart.update_layout(
            height=2000,
            title_text="Average suicide per 100k population",
            title_font_size=18,
            title_font_color='white',
            title_x=0.5,
            title_y=0.99,
            title_xanchor="center",
            title_yanchor='top',
            margin_l=100,
            xaxis_title='Suicide  per  100  Pop',
            xaxis_titlefont_size=16,
            xaxis_title_standoff=50,
            yaxis_title='Country',
            yaxis_titlefont_size=16,
            yaxis_title_standoff=20,

        )

    return country_bar_chart

@app.callback([Output('country-line','figure'),
               Output('country-line-sex', 'figure'),
               Output('country-line-age','figure'),
               Output('country-pie-sex','figure'),
               Output('country-pie-age','figure')],
              [Input('country-list','value'),
               Input('range-year','value'),
               Input('tabs','value')])
def display_country_charts(country, year,tab):

    y = year
    country_charts_df = df[(df['Country'] == country) & (df['Year'] >= y[0]) & (df['Year'] <= y[1])]
    country_line_df = country_charts_df.groupby(['Year'], as_index=False).sum()
    country_line_sex_df = country_charts_df.groupby(['Year', 'Sex'], as_index=False).sum()
    country_line_age_df = country_charts_df.groupby(['Year', 'Age'], as_index=False).sum()
    country_pie_sex_df = country_charts_df.groupby(['Sex'], as_index=False).sum()
    country_pie_age_df = country_charts_df.groupby(['Age'], as_index=False).sum()
    # ----------------------------------------------- #
    # country line chart
    country_line_plot = plotly.line(
        country_line_df,
        height= 600,
        x='Year',
        y='Suicides_100k_Pop',
        template='plotly_dark'
    )

    country_line_plot.update_traces(
        hovertemplate="Suicide Number = %{y} <br> Year = %{x}"
    )

    country_line_plot.update_layout(
        title_text="Average suicide per 100k population",
        title_font_size=18,
        title_font_color='white',
        title_x=0.5,
        title_y=0.95,
        title_xanchor="center",
        title_yanchor='top',
        margin_l=100,
        xaxis_title='Years',
        xaxis_titlefont_size=16,
        xaxis_title_standoff=50,
        yaxis_title='Suicide  per  100  Pop',
        yaxis_titlefont_size=16,
        yaxis_title_standoff=30,

    )
    # ------------------------------------------------------------ #
    # Country line plot by gender
    country_line_sex_plot = plotly.line(
        country_line_sex_df,
        height= 500,
        x='Year',
        y='Suicides_100k_Pop',
        color='Sex',
        template='plotly_dark'
    )

    country_line_sex_plot.update_traces(
        hovertemplate="Suicide Number = %{y} <br> Year = %{x}"
    )

    country_line_sex_plot.update_layout(
        title_text="Average suicide per 100k population by gender",
        title_font_size=18,
        title_font_color='white',
        title_x=0.5,
        title_y=0.95,
        title_xanchor="center",
        title_yanchor='top',
        margin_l=100,
        xaxis_title='Years',
        xaxis_titlefont_size=16,
        xaxis_title_standoff=50,
        yaxis_title='Suicide  per  100  Pop',
        yaxis_titlefont_size=16,
        yaxis_title_standoff=30,

    )
    # ------------------------------------------------------------#
    # country line plot by age

    country_line_age_plot = plotly.line(
        country_line_age_df,
        height=500,
        x='Year',
        y='Suicides_100k_Pop',
        color='Age',
        template='plotly_dark'
    )

    country_line_age_plot.update_traces(
        hovertemplate="Suicide Number = %{y} <br> Year = %{x}"
    )

    country_line_age_plot.update_layout(
        title_text="Average suicide per 100k population by age",
        title_font_size=18,
        title_font_color='white',
        title_x=0.5,
        title_y=0.95,
        title_xanchor="center",
        title_yanchor='top',
        margin_l=100,
        xaxis_title='Years',
        xaxis_titlefont_size=16,
        xaxis_title_standoff=50,
        yaxis_title='Suicide  per  100  Pop',
        yaxis_titlefont_size=16,
        yaxis_title_standoff=30,

    )
    # ------------------------------------------------------------- #
    # Country pie chart by gender
    country_pie_sex_plot = plotly.pie(country_pie_sex_df,
                                   values='Suicide',
                                   names='Sex',
                                   template='plotly_dark',
                                   title='Country Suicide by gender',
                                   height=480
                                      )

    country_pie_sex_plot.update_traces(textposition='inside', textinfo='percent+label', textfont_size=16)
    # -------------------------------------------------------------- #
    # Country pie chart by age
    country_pie_age_plot = plotly.pie(country_pie_age_df,
                                   values='Suicide',
                                   names='Age',
                                   template='plotly_dark',
                                   title='Country Suicide by age',
                                   height=480)

    country_pie_age_plot.update_traces(textposition='inside', textinfo='percent+label', textfont_size=12)
    # -------------------------------------------------------------- #


    return country_line_plot, country_line_sex_plot, country_line_age_plot, country_pie_sex_plot, country_pie_age_plot

    if tab == 'tab-2':
        return country_line_plot.update_layout(height = 500), \
               country_line_age_plot.update_layout(height = 500), \
               country_line_age_plot.update_layout(height = 500), \
               country_pie_sex_plot.update_layout(height =480),\
               country_pie_age_plot.update_layout(height = 480),






