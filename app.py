import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configurações iniciais
st.set_page_config(page_title="Kite For Life - Dashboard", layout="wide")

# Lista de critérios identificados na sua planilha
CRITERIOS = [
    'LIDERANÇA', 'ASSIDUIDADE', 'FLEXIBILIDADE', 'TEORIA', 
    'COMANDO ', 'CONTROLE', 'BADYDRAG ESQ/DIR', 'WATER START', 
    'PRANCHA ESQ/DIR', 'CONTRA VENTO'
]

# Sidebar - Menu
st.sidebar.title("KITE FOR LIFE 2025")
menu = st.sidebar.radio("Navegação", ["Visão Geral (Escola)", "Análise por Aluno", "Registar Avaliação"])

# Simulação de carregamento de dados (Baseado no seu ficheiro 'Aval')
# No uso real: df = pd.read_csv("seu_arquivo_aval.csv")
data = {
    'Aluno': ['Beatriz Vitoria', 'Ana Cecilia', 'Francisco Neto', 'César Eduardo',]
    'LIDERANÇA': [4, 2, 3, 2],
    'ASSIDUIDADE': [3, 4, 5, 4],
    'CONTRA VENTO': [3, 1, 4, 1],
    'Média Geral': [3.0, 2.0, 3.9, 2.0]
}
df = pd.DataFrame(data)

if menu == "Visão Geral (Escola)":
    st.title("📊 Painel de Desempenho da Escola")
    
    # Métricas Principais
    m1, m2, m3 = st.columns(3)
    m1.metric("Média Geral da Escola", "2.26")
    m2.metric("Total de Alunos", len(df))
    m3.metric("Melhor Critério", "Assiduidade")

    # Gráfico de Médias por Critério
    st.subheader("Desempenho por Habilidade")
    # Aqui usamos os dados do seu 'Dash2'
    avg_data = pd.DataFrame({
        'Critério': CRITERIOS,
        'Média': [2.24, 3.35, 2.47, 2.18, 2.18, 2.12, 2.47, 2.06, 1.88, 1.71]
    })
    fig_bar = px.bar(avg_data, x='Critério', y='Média', color='Média', color_continuous_scale='Blues')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    

elif menu == "Análise por Aluno":
    st.title("👤 Evolução Individual")
    nome_aluno = st.selectbox("Escolha o aluno:", df['Aluno'])
    
    # Gráfico de Radar para Performance
    # Compara o aluno selecionado com a média (2.26)
    fig = go.Figure()
    
    # Valores do aluno (exemplo estático para ilustração)
    values_aluno = [4, 3, 3, 2, 2, 2, 4, 4, 3, 3] 
    media_escola = [2.26] * 10

    fig.add_trace(go.Scatterpolar(r=values_aluno, theta=CRITERIOS, fill='toself', name='Aluno'))
    fig.add_trace(go.Scatterpolar(r=media_escola, theta=CRITERIOS, fill='toself', name='Média Escola', fillcolor='rgba(200, 200, 200, 0.3)'))

    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
    
    

elif menu == "Registar Avaliação":
    st.title("📝 Novo Registo de Notas")
    with st.form("form_notas"):
        aluno = st.selectbox("Selecione o Aluno", df['Aluno'])
        cols = st.columns(2)
        
        # Gera sliders automaticamente para cada critério
        for i, crit in enumerate(CRITERIOS):
            with cols[i % 2]:
                st.slider(crit, 1, 5, 3)
        
        st.text_area("Pontos a Melhorar/Desenvolver")
        if st.form_submit_button("Submeter Avaliação"):

            st.success(f"Avaliação de {aluno} guardada com sucesso!")



