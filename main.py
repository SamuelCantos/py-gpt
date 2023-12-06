#Creando una terminal para interactuar con chat gpt y mantener una conversacion fluida con contexto y memoria. 
# ---- El programa tiene un limite de uso. 



import openai
import config


def main():


    openai.api_key = config.api_key

        #contexto del asistente para iniciar
    messages =[{'role': 'system',
                'content': 'sos un asistente, el mejor de todos!'}]

    while True:

        content = input('sobre que te gustaria hablar?: ').lower()

        if content.lower()  == 'exit':
            break
            #guardamos las preguntas del usuario
        messages.append({'role': 'user',
                            'content':content})

        response = openai.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
            )   
            
        response_content = response.choices[0].message.content

            #guardamos las respuestas del asistente
        messages.append({
            'role': 'assistant',
            'content': response_content,
        })


        print(response_content)


if __name__ == "__main__":
    typer.run(main)





