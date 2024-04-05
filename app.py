import streamlit as st
from streamlit_tags import st_tags
import parse


col1, col2, col3 = st.columns([1,6,1])

with col2:
    # Title
    st.title("GemXtract")

    # Text input for URL
    url = st.text_input('Enter the URL to parse:', '')
    attributes = st_tags(
        label='Enter attributes to extract: ',
        text='Press enter to add more',
        )

    # Fetch and display button
    if st.button('Parse', use_container_width=True):
        if url:
            parsed_html = parse.get_html(url)
            tags = parse.parse_info(None, attributes)

            st.text_area('Attributes', value=tags, height=100)
        else:
            st.error('Please enter a URL.')


st.code(parsed_html, language="markup", line_numbers=True)


