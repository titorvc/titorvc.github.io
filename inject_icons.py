import re

html_file = "/home/titorvc/.gemini/antigravity/scratch/Portfolio_Landing/index.html"
with open(html_file, 'r') as f:
    content = f.read()

openai_svg = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" title="OpenAI"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"/></svg>'
whatsapp_svg = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" title="WhatsApp"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.666.598 1.236.771 1.41.858.173.086.275.072.376-.043.101-.115.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-3.825 3.113-6.937 6.937-6.937 1.856.001 3.598.723 4.907 2.034 1.31 1.311 2.031 3.054 2.03 4.908-.001 3.825-3.113 6.938-6.937 6.938z"/></svg>'

icons = {
    "WhatsApp Barber AI Bot": f'<div class="project-tech-icons">\n                        <img src="assets/n8n_logo.png" alt="n8n" title="n8n" style="object-fit: contain;">\n                        <i class="devicon-google-plain" title="Google Gemini"></i>\n                        {whatsapp_svg}\n                    </div>',
    "Estudio Correlacional UADY": '<div class="project-tech-icons">\n                        <i class="devicon-r-plain" title="R"></i>\n                        <i class="devicon-python-plain" title="Python/Pandas"></i>\n                    </div>',
    "Job Hunter AI": '<div class="project-tech-icons">\n                        <i class="devicon-apache-plain" title="Apache Airflow"></i>\n                        <i class="devicon-python-plain" title="Python"></i>\n                        <i class="devicon-linux-plain" title="Linux"></i>\n                    </div>',
    "AgenMono": f'<div class="project-tech-icons">\n                        <i class="devicon-python-plain" title="Python"></i>\n                        {openai_svg}\n                    </div>',
    "Nexus OS Integration": '<div class="project-tech-icons">\n                        <i class="devicon-linux-plain" title="Linux"></i>\n                        <i class="devicon-bash-plain" title="Bash"></i>\n                        <i style="font-style: normal; font-size: 1.5rem; filter: grayscale(100%); line-height: 1;" title="Obsidian">💎</i>\n                    </div>',
    "Capacitación USAER con ChatGPT": f'<div class="project-tech-icons">\n                        {openai_svg}\n                    </div>',
    "Riesgos de Pantallas en Preescolar": '<div class="project-tech-icons">\n                        <i class="devicon-html5-plain" title="Presentación Interactiva"></i>\n                    </div>',
    "Machine Learning para Vinilos": f'<div class="project-tech-icons">\n                        <i class="devicon-python-plain" title="Python"></i>\n                        {openai_svg}\n                    </div>',
    "Arquitectos del Pensamiento": '<div class="project-tech-icons">\n                        <i class="devicon-python-plain" title="Machine Learning"></i>\n                    </div>'
}

for title, html_str in icons.items():
    # Find the title <h3>...</h3> and insert icons right after
    pattern = rf"(<h3>{title}</h3>)"
    content = re.sub(pattern, rf"\1\n                    {html_str}", content)

with open(html_file, 'w') as f:
    f.write(content)

print("Icons injected!")
