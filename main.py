import streamlit as st
from circle import Circle

if __name__ == '__main__':
    st.write("# Circle")
    radius = st.slider("Radius:", max_value=1.0, min_value=0.0, step=0.01, value=0.5)

    circle = Circle(radius=radius)
    st.bokeh_chart(circle.render_shape())