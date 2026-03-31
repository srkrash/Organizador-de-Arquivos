import PySimpleGUI as sg
import os
import shutil
import warnings as w

class MainScreen:

    key_in_dir: str = 'dir'
    key_btn_organize: str = 'btn_organize'
    
    def __init__(self) -> None:
        self.control: Main = Main()
        sg.theme('DefaultNoMoreNagging')
        
    def mainLayout(self) -> list[list[sg.Element]]:
        return [
            [sg.Text('Organizador de arquivos', font=(
                'Arial', 24), justification='center')],
            [sg.HorizontalSeparator()],
            [sg.T()],
            [sg.Text('Diretório:'), sg.InputText(key=self.key_in_dir),
             sg.FolderBrowse('Selecionar')],
            [sg.T()],
            [sg.Button('Organizar', key=self.key_btn_organize, button_color='green', expand_x=True)],
        ]
        
    def open_window(self) -> None:
        layout: list[list[sg.Element]] = self.mainLayout()
        window: sg.Window = sg.Window('Organizador de arquivos', layout=layout, finalize=True, icon='logo.ico')
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == self.key_btn_organize:
                n_categories: int = self.control.organize_by_type(values[self.key_in_dir])
                sg.popup(f'Foram organizadas {n_categories} categorias de arquivos com sucesso!', title='Organizador de arquivos', icon='logo.ico')
            
class Main:
    def __init__(self) -> None:
        pass
        
    def organize_by_type(self, dir: str) -> int:
        """
        Organizes files in a directory by category.

        Args:
            dir (str): The directory to organize.

        Returns:
            int: The number of distinct categories created.

        Raises:
            FileNotFoundError: If the directory does not exist.
            OSError: If there is an error creating a new directory.
            OSError: If there is an error moving a file.
        """
        categories = {
            'Imagens': ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp', '.svg'],
            'Audios': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
            'Vídeos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg'],
            'Documentos': ['.txt', '.xlsx', '.xls', '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.rtf', '.csv'],
            'Arquivos e Instaladores': ['.exe', '.msi', '.zip', '.rar', '.7z', '.tar', '.gz', '.pkg', '.deb', '.rpm', '.iso']
        }

        # Check if directory exists
        if not os.path.exists(dir):
            raise FileNotFoundError(f'Directory {dir} does not exist.')

        categories_created: set = set()

        # Iterate over files in the directory
        for file in os.listdir(dir):
            item_path = os.path.join(dir, file)
            
            # Check if the item is a file
            if not os.path.isfile(item_path):
                continue
            
            # Get the file extension in lowercase
            ext = os.path.splitext(file)[1].lower()

            # Find the target category
            target_category = 'Outros'
            for cat, extensions in categories.items():
                if ext in extensions:
                    target_category = cat
                    break

            new_dir = os.path.join(dir, target_category)
            if not os.path.exists(new_dir):
                try:
                    os.makedirs(new_dir)
                except OSError as error:
                    raise OSError(f'{error}: {new_dir}')

            # Move the file to the new directory
            try:
                shutil.move(item_path, os.path.join(new_dir, file))
                categories_created.add(target_category)
            except OSError as error:
                w.warn(f'{error}: {file}\n{categories_created}')

        return len(categories_created)
        
    def run(self) -> None:
        MainScreen().open_window()

if __name__ == '__main__':
    Main().run()