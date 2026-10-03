import re

html_file = "/home/titorvc/.gemini/antigravity/scratch/Portfolio_Landing/index.html"
with open(html_file, 'r') as f:
    content = f.read()

# The pattern needs to match:
# <span class="badge">...</span>
# <h3>...</h3>
# <div class="project-tech-icons">...</div>

# We want to change it to:
# <div class="project-header-top">
#     <span class="badge">...</span>
#     <div class="project-tech-icons">...</div>
# </div>
# <h3>...</h3>

pattern = re.compile(
    r'(<span class="badge">.*?</span>)\s*'
    r'(<h3>.*?</h3>)\s*'
    r'(<div class="project-tech-icons">.*?</div>)',
    re.DOTALL
)

def replacer(match):
    badge = match.group(1)
    h3 = match.group(2)
    icons = match.group(3)
    return f'<div class="project-header-top">\n                        {badge}\n                        {icons}\n                    </div>\n                    {h3}'

new_content = pattern.sub(replacer, content)

with open(html_file, 'w') as f:
    f.write(new_content)

print("HTML reordered!")
