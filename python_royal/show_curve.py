import sys

import pandas as pd
import streamlit as st

if __name__ == "__main__":
    name = sys.argv[1]
    df = pd.read_csv(f"data/{name}.csv")
    fig = {
        "data": [
            {
                "type": "bar",
                "x": tuple(range(len(df))),
                "y": df[df.columns[0]],
            }
        ],
        "layout": {"title": {"text": name.upper()}},
    }
    st.title(f"Barchart for {name.upper()}")
    st.plotly_chart(figure_or_data=fig)
