import re

html_file = "/home/titorvc/.gemini/antigravity/scratch/Portfolio_Landing/index.html"
with open(html_file, 'r') as f:
    content = f.read()

# Fix n8n logo class
content = content.replace(
    '<img src="assets/n8n_logo.png" alt="n8n" title="n8n" style="object-fit: contain;">',
    '<img src="assets/n8n_logo.png" alt="n8n" title="n8n" class="n8n-logo" style="object-fit: contain;">'
)

# Insert <span class="tech-plus">+</span> between icons in project-tech-icons
def insert_plus(match):
    inner_html = match.group(1)
    # find all icon tags
    # they are either <img ...>, <i ...>...</i>, or <svg ...>...</svg>
    # Since we know exactly how they look, we can just split by newline, strip, filter empty, and join
    lines = [line.strip() for line in inner_html.split('\n') if line.strip()]
    
    # But wait, svg might be multiple lines if formatted differently.
    # In my previous script, I inserted them as single lines. Let's verify.
    # Actually, it's safer to just split by '><' or similar?
    # Since I generated them, they are one per line.
    
    if len(lines) > 1:
        new_inner = '\n                        <span class="tech-plus">+</span>\n                        '.join(lines)
        return f'<div class="project-tech-icons">\n                        {new_inner}\n                    </div>'
    return match.group(0)

# Replace
pattern = re.compile(r'<div class="project-tech-icons">\s*(.*?)\s*</div>', re.DOTALL)
content = pattern.sub(insert_plus, content)

with open(html_file, 'w') as f:
    f.write(content)

print("Icons fixed!")
