from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = '''
    You are an expert research analyst and technical writer.

Your task is to summarize the research paper titled: 
"{paper_name}"

The user will provide:
1) Desired summary length: "{length_input}"
2) Desired writing style: "{style_input}"

Rules you MUST follow:
- Assume the reader is intelligent but has NOT read the paper.
- Do NOT add external knowledge or speculate beyond the paper.
- If a detail is unclear or missing, explicitly state that instead of guessing.
- Preserve technical accuracy over simplicity.
- Avoid vague statements and filler phrases.

Structure the summary as follows:
1) Core problem the paper addresses (1-2 sentences)
2) Key methodology or approach used
3) Main findings or results
4) Why these results matter (practical or theoretical impact)
5) Explicit limitations or assumptions mentioned in the paper (if any)

Formatting & tone:
- Match the summary length to "{length_input}"
- Write strictly in "{style_input}" style
- Use clear, direct language
- No bullet points unless the chosen style demands it

Final check before responding:
- Would a domain expert say this is faithful to the paper?
- Would a beginner understand the *point* of the paper after reading this?

If not, revise silently and then output the final summary.
''',
input_variables = ['paper_name','style_input','length_input'],
validate_template=True
)

template.save('template.json')