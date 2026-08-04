import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f4f4",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[
        html.H1(
            "Pink Morsels Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#d63384"
            }
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={
                "textAlign": "center",
                "marginBottom": "20px"
            }
        ),

        dcc.Graph(id="sales-chart")
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[df["Region"].str.lower() == region]

    sales = filtered.groupby("Date", as_index=False)["Sales"].sum()

    fig = px.line(
        sales,
        x="Date",
        y="Sales",
        title="Pink Morsels Sales",
        labels={
            "Date": "Date",
            "Sales": "Sales"
        }
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f4f4",
        font=dict(size=15)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)