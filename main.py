import subprocess
import click
import os

@click.command()
@click.option('--path', '-p', prompt='Путь', help='Путь к папке')
@click.option('--quality', '-q', prompt='Качество сжатия', default=70,
            help='Качество сжатия, по умолчанию 70')        
def run(path, quality):
    for address, _, files in os.walk(path):
        for file in files:
            try:
                if file.split('.')[1].lower() in ['jpg', 'jpeg'] and file[:5] != 'MozJ_':
                    click.echo(f'{address}\{file}')
                    subprocess.run(f'Release\cjpeg.exe\
                                -quality {quality} "{address}\{file}" >\
                                "{address}\MozJ_{file}"', check=True, shell=True)
                    os.remove(f'{address}\{file}')
            except Exception as e:
                click.echo(e)

if __name__ == '__main__':
    run()