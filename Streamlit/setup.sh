mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"koppineedi.suryanagavijayadurgakalyan.18cse@bmu.edu.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml