## Introduction
The purpose of this project is to experiment with building a local version of a generative AI chatbot. Generative AI chatbots, such as ChatGPT and Google Bard, are becoming increasingly popular in the tech space. Many companies are building their own large language models (LLMs) and AI assistants to meet their specific needs. Tapping into the power of generative AI has the potential to improve efficiency and learning in a variety of fields. This application takes user input, searches the web using Google for the most accurate response and writes it into a streamlit interface.

## Process
For this project, I used an OpenAI API to utilize GPT-3 to generate the search input and result as well as Google API to search the web. Once the user inputs their question, LangChain utilizes OpenAI to generate a simplified search statement to input into Google based on the user input. By initializing a LangChain agent for searching Google, this process becomes extremely simple to code while getting very good results.

## Results
<p align="center">
  <img src="https://github.com/leeharry709/generative-nlp-chatbot/blob/main/lanchain_agents_ss.png?raw=true" width='75%'>
</p>
The search gave some very interesting results. The first question was answered most accurately, explaining the use of the third eyelid. users would then be able to interpret taht cats have three eyelids to protect their eyes and keep them moist. The second question is incorrect according to Politico.com, which states that Trump has been indicted on 34 felony counts in connection with hush money payments, not falsifying business records in New York. It seems it many have pieced it all together based on various news articles. The third and fourth responses are most interested to me. Without the dat input, the chatbot gave me when the lowest price $SPY was at in October 2022. But, by giving it a specific date to search for, it gave me the right answer.

## Conclusions
AI learning is still in its infancy. While the technology is there and generative AI is possible, it isn't completely soundproof yet. Inaccuracy can cause misinformation in these types of bots, and users would require more accuracy and reliablility to have it truly add value into their lives. With more fine-tuning into how OpenAI generates search results, more accurate responses could be generated. It all would come down to fully understand how OpenAI generates its search results, how Google utilizes the search input to generate its results, and how OpenAI summarizes the search results into a cohesive response. 
