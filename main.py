import streamlit as st

# Configuração da página (título, ícone e layout)
st.set_page_config(
    page_title="Processamento de Dados & Automação",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização minimalista customizada (CSS)
st.markdown("""
    <style>
    /* Oculta menus padrão do Streamlit para parecer um site */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Ajuste de margens e tipografia */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
    }
    h1, h2, h3 {
        font-family: 'Segoe UI', Roboto, sans-serif;
        color: #1E293B;
    }
    p, li {
        color: #475569;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    
    /* Card de Contato */
    .contact-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 24px;
        text-align: center;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO / HERO ---
st.title("Transforme seus Dados em Eficiência Operacional")
st.subheader("Soluções acessíveis de automação e processamento de dados para pequenas empresas.")

st.divider()

# --- SOBRE NÓS ---
st.markdown("""
Ajudamos pequenas e médias empresas a eliminarem tarefas manuais repetitivas, estruturarem seus dados 
e tomarem decisões estratégicas mais rápidas com relatórios automatizados.
""")

st.write("")

# --- SERVIÇOS & IMAGENS ---
st.header("Nossos Serviços")

# Layout responsivo em 2 colunas para desktop (no mobile empilha automaticamente)
col1, col2 = st.columns(2, gap="large")

with col1:
    # Substitua o link pela imagem do seu serviço 1 ou caminho local
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800", use_container_width=True)
    st.caption("Visualização de Dados e Dashboards")
    
    st.markdown("""
    ### Processamento & BI
    * **Limpeza e Estruturação:** Organização de planilhas e bancos de dados bagunçados.
    * **Dashboards Interativos:** Painéis de acompanhamento em tempo real para sua gestão.
    * **Integridade dos Dados:** Padronização de dados financeiros e operacionais.
    """)

with col2:
    # Substitua o link pela imagem do seu serviço 2 ou caminho local
    st.image("https://images.unsplash.com/photo-1518186285589-2f7649de83e0?q=80&w=800", use_container_width=True)
    st.caption("Automação de Fluxos de Trabalho")
    
    st.markdown("""
    ### Automação de Processos
    * **Integração de Sistemas:** Conexão entre softwares, ERPs e planilhas.
    * **Relatórios Automáticos:** Geração e envio automático de relatórios por e-mail ou WhatsApp.
    * **Eliminação de Tarefas Manuais:** Scripts sob medida para economizar horas de trabalho da sua equipe.
    """)

st.divider()

# --- CONTATO / CALL TO ACTION ---
st.header("Entre em Contato")
st.write("Pronto para otimizar os processos da sua empresa? Fale conosco para uma avaliação sem compromisso.")

# Card destacado para conversão
st.markdown("""
    <div class="contact-card">
        <h3>Fale Conosco</h3>
        <p><strong>E-mail:</strong> contato@suaempresa.com.br</p>
        <p><strong>WhatsApp:</strong> (00) 99999-9999</p>
        <p><strong>Horário de Atendimento:</strong> Segunda a Sexta, das 8h às 18h</p>
    </div>
""", unsafe_allow_html=True)