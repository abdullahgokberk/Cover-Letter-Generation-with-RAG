from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0)

system_prompt = ChatPromptTemplate.from_messages([
    ("system", """You're an assistant who creates a short, effective cover letter based on the user's CV and the job they're applying for.
    When the user submits a job posting, generate a personalized cover letter tailored to the job posting, based on the skills and experience in their CV.
    Provide the same cover letter in both English and Turkish and keep the answer concise.
    
    Question: {question}
    Context: {context}
    
    Answer:
    """)
])

generation_chain = system_prompt | llm | StrOutputParser()

