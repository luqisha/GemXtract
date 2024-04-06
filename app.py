import streamlit as st
import parse
from streamlit_tags import st_tags

response = None
output = None

col1, col2, col3 = st.columns([1,6,1])

with col2:
    # Title
    st.title('GemXtract')

    # Text input for URL
    url = st.text_input('Enter the URL to parse:', '')

    # Tags input for Atributes
    attributes = st_tags(
        label='Enter attributes to extract: ',
        text='Press enter to add more',
        )

    # Fetch button
    if st.button('Parse', use_container_width=True):
        if url:
            parsed_html = parse.get_html(url)
            response = parse.parse_info(parsed_html, attributes)

            output = parse.sanitize(response[0]['generated_text'])
            print(output)

        else:
            st.error('Please enter a URL.')

# # For DEBUGGING
# if response:
#     st.text(response[0]['generated_text'])

# Display the JSON output
if output:
       st.code(output, language='json')
