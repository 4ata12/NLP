
from gensim.summarization.summarizer import summarize 
# Paragraph
paragraph = "Natural language processing (NLP) is the ability of a computer program to understand human language as it is spoken. NLP is a component of artificial intelligence (AI). The development of NLP applications is challenging because computers traditionally require humans to 'speak' to them in a programming language that is precise, unambiguous and highly structured, or through a limited number of clearly enunciated voice commands. Human speech, however, is not always precise -- it is often ambiguous and the linguistic structure can depend on many complex variables, including slang, regional dialects and social context."
# Getting the Summary of the text based on percentage (0.5% of the original content). 
summ_per = summarize(paragraph, ratio = 0.5) 
print("Percent summary:") 
print(summ_per) 
# Getting the summary of the text based on number of words (50 words) 
summ_words = summarize(paragraph, word_count = 50) 
print("\n")
print("Word count summary:") 
print(summ_words)
print("\n")
print("Ahmad Esmail Abu-Elftooh Shata") 
print("\n")
print("800125687")