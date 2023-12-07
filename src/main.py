#Creando una terminal para interactuar con chat gpt y mantener una conversacion fluida con contexto y memoria. 
# ---- El programa tiene un limite de uso. 
#06-12-23

import os
from dotenv import load_dotenv
import openai 
import typer
from rich import print
from rich.table import Table

load_dotenv()

api_key = os.getenv('API_KEY')


def main():
    
    openai.api_key = api_key

    print("[bold magenta] Hola soy chatGPT integrado en una aplicacion de python creado por Samuel [/bold magenta]")



    table = Table('comand', 'Descript') 
    table.add_row('exit', 'salir de la aplicacion')
    table.add_row('clear', 'limpiar la conversacion y borrar su memoria')
    print(table)



    #contexto del asistente para iniciar
    context = {'role': 'system',
               'content': 'sos el mejor asistente del universo'}

        
    messages = [context]

    while True:

        content = _prompt()

        
        if content == 'clear':
            print('[violet]procedere a limpiar mi memoria[/violet]')
            messages=[context]
            content = _prompt()

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


        print(f"> {response_content}")


def _prompt(): 

    prompt = typer.prompt('\nsobre que te gustaria hablar?: ').lower()

    if prompt == 'exit':
       exit = typer.confirm('estas seguro de cerrar el programa?')
    #deteniendo la ejecucion de typer, con esto vamos a dejar de correr el programa por completo al tipear exit
       if exit:
            print('\n [blue] hasta la proxima![/blue]\n')
            raise typer.Abort()
       return _prompt()
    return prompt


if __name__ == "__main__":
    typer.run(main)





