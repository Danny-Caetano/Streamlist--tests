import streamlit as st
from json import loads
from pandas import read_csv



st.markdown('''
# Exibidor de arquivos
            
## Suba seu arquivo aqui e veja o que acontece    
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['jpg', 'png', 'py', 'json', 'wav', 'csv']
)

st.text_input('Email')
st.text_input('Senha', type='password')

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'aplication', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
            st.line_chart(df)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'audio', _:
            st.audio(arquivo)
else:
    st.error('Ainda não tenho um arquivo!')