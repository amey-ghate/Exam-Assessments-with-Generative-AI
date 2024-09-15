import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

#define rounding function
def myround(x, base=0.5):
    return int(base * round(float(x)/base))

#Define age mapping function
def student_age(x):
    ageMapping = {}
    for i in range(12):
        ageMapping[i] =6+i
    return ageMapping[x]

#define output model
class checkedAnswer(BaseModel):
    highlights: list =Field(description='list of accurate information contained in the answer')
    improvementAreas: list = Field(description='list of possible improvements in answer')
    score: int =Field(description='answer score')

parser =PydanticOutputParser(pydantic_object=checkedAnswer)

# Streamlit UI setup
st.title("Exam Assessments with Gen AI")

# User inputs for model and answer text
model_text = st.text_area("Enter the model answer", height=50)
answer_text = st.text_area("Enter the student answer", height=50)
subject = st.text_input("Enter the Subject")
standard = st.number_input("Enter the standard of student", min_value=1, max_value=12, step=1)
marks = st.number_input("Enter marks for the question", min_value=1, max_value=10, step=1)


# Button to process the comparison
if st.button("Check Answer"):
    if model_text and answer_text and subject and standard and marks:
        # message template for Model and student answer
        age = student_age(standard)
        
        message = """ 
        {context}
        You are an expert {subject} teacher in charge of checking the answer of a {standard} standard student of age {age} years
        
        There are two texts given. One of them is model_answer which is expected answer. The other one is the student_answer the answer provided by the  student
        Analyze student_answer as compared to model_answer to identify 
        1. provide maximum of 3 information from model_answer that is accurately articulated in the student_answer
        2. provide maximum 3 possible improvements in student_answer ordered with most critical as first
        The model_answer is:
        <model_answer>{model}</model_answer>
        The student_answer is:
        <student_answer>{answer}</student_answer>

        take student age into account while comparing student_answer with model_answer
        {input}
        Provide the assessment as only a JSON output with the following format:
        {{"highlights": "list of information from model_answer that is accurately articulated in the student_answer", 
          "improvementAreas": "list of possible improvements in student_answer ordered with most critical as first", 
          "score": "score on rating for 10"}}
        """

        # Create the ChatPromptTemplate
        prompt = ChatPromptTemplate.from_template(message)

        # Define the context and input
        context = "You are teacher in charge of checking the answers"
        input_text = "Rate the coverage of information the student_answer in comparison to the model_answer on a scale from 1 to 10, where 1 means no information is covered and 10 means all information is covered."

        # Define the language model
        llm = Ollama(model="llama3.1", temperature=0.7, num_ctx=4096)

        chain = prompt | llm |parser

        informationResponse = chain.invoke({"context":context, "input":input_text, "model":model_text, "answer":answer_text, "subject":subject, "standard":standard, "age":age })

        # Print the response
        print(f"response={informationResponse}")
        # Prepare the input for the prompt
        #prompt_input = prompt.format(model=model_text, answer=answer_text, context=context, input=input_text, subject=subject,standard=standard )

        st.write(informationResponse)


        # message template for language
        message = """
                    {context}
                    You are an expert {subject} teacher with good knowledge of english in charge of checking the answer of a {standard} standard student of age {age} years.

                    There is student answer given below. Analyse it for its language construct and grammer 
                    Analyze student_answer as compared to model_answer to identify 
                    1. good language constructs contained in the student_answer
                    2. provide maximum 3 language improvements opportunities in student_answer ordered with most critical as first
                    <student_answer>{answer}</student_answer>
                    take student age into account while comparing student_answer with model_answer
                    {input}    
                    Provide the assessment as only a JSON output with the following format:
        {{"highlights": "list of language constructs used in the answer", "improvementAreas": "list of possible improvements in answer language", "score": "score on rating for 10"}}
        """

        # Create the ChatPromptTemplate
        Language_prompt = ChatPromptTemplate.from_template(message)

        # Define the variables
        context = "You are an expert teacher"
        input_text = "rate the language consistancy and grammer on a scale from 1 to 10, where 1 means language is incomprehensible  or poor grammer. 10 means flawless text."

        chain = Language_prompt | llm |parser
        languageResponse = chain.invoke({"context":context, "input":input_text, "answer":answer_text, "subject":subject, "standard":standard, "age":age })
        st.write(languageResponse)

        # Print the response
        finalMarks = myround((((informationResponse.score * 0.8 + languageResponse.score * 0.2) * marks )/ 10))
        st.write("Marks for the answer is")
        st.write(finalMarks)

        st.write("Areas for improvement is")
        st.write(informationResponse.improvementAreas)
        
    
    else:
        st.error("Please provide both the model text and the answer text.")
