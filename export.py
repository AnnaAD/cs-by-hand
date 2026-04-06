import pypandoc

header = r"""\documentclass{article}
\usepackage{graphicx} % Required for inserting images
\usepackage[margin=1in,footskip=0.25in]{geometry}

\newcommand{\pandocbounded}[1]{\begin{center}#1\end{center}}

\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}

\title{cs-by-hand-format}
\author{Anna Arpaci-Dusseau}
\date{April 2026}

\begin{document}

\maketitle
"""


folders = ["lec0-1", "lec2", "lec3", "lec4"]

output = header
for folder in folders:
    with open(f'{folder}/README.md', 'r') as file:
        content = file.read()
        print(content)

        latex_output = pypandoc.convert_text(content, 'latex', format='md')
        output += latex_output
        output += r"\newpage"
        output += "\n"

output = output.replace("../output", "output")
output += "\end{document}"
with open("output.tex", "w") as file:
    file.write(output)


# # Convert a markdown file to a .tex file
# pypandoc.convert_file('input.md', 'latex', outputfile="output.tex")