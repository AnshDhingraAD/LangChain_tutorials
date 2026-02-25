# recursive character text splitter -> mostly used
# para -> \n\n
# sent -> \n
# word -> " "
# char -> ""

# it keeps on beaking accoring to above heirrachical order and if chunks are too small then it starts merging , it prevents cutting of words.
 
from langchain_text_splitters import RecursiveCharacterTextSplitter

text='''Artificial Intelligence has transformed the way humans interact with technology. From voice assistants that understand natural language to recommendation systems that predict user preferences, AI is now deeply integrated into everyday life. Companies across industries are investing heavily in machine learning models to automate tasks, improve efficiency, and extract insights from massive datasets.

In healthcare, AI-powered diagnostic systems assist doctors in detecting diseases at early stages. Computer vision models analyze medical images such as X-rays and MRIs with remarkable accuracy. Similarly, in finance, fraud detection algorithms monitor transaction patterns in real time to flag suspicious activities. These advancements not only reduce human error but also save valuable time.

Education is another sector witnessing rapid AI adoption. Intelligent tutoring systems personalize learning experiences based on student performance. Natural Language Processing enables automated essay grading, chatbot tutors, and real-time translation, making education more accessible globally.

However, the rise of AI also raises ethical concerns. Issues such as data privacy, algorithmic bias, and job displacement are widely debated. Experts emphasize the importance of responsible AI development, transparency in model decisions, and regulations to ensure technology benefits society as a whole.

Looking ahead, the future of AI holds even greater possibilities. With advancements in generative models, robotics, and multimodal systems, machines are becoming more creative and context-aware. The collaboration between humans and intelligent systems is expected to redefine innovation in the coming decades.'''

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks=splitter.split_text(text)

print(chunks)
print(len(chunks))
