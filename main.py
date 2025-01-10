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
                n_types: int = self.control.organize_by_type(values[self.key_in_dir])
                sg.popup(f'Foram organizados {n_types} tipos de arquivos com sucesso!', title='Organizador de arquivos', icon='logo.ico')
            
class Main:
    def __init__(self) -> None:
        pass
        
    def organize_by_type(self, dir: str) -> int:
        """
        Organizes files in a directory by type.

        Args:
            dir (str): The directory to organize.

        Returns:
            int: The number of distinct file types found.

        Raises:
            FileNotFoundError: If the directory does not exist.
            OSError: If there is an error creating a new directory.
            OSError: If there is an error moving a file.
        """
        # List to store distinct file types
        types: list[str] = []

        # Check if directory exists
        if not os.path.exists(dir):
            raise FileNotFoundError(f'Directory {dir} does not exist.')

        # Iterate over files in the directory
        for file in os.listdir(dir):
            
            # Check if the file is a directory
            if os.path.isdir(f'{dir}/{file}'):
                continue
            
            # Get the file extension in uppercase
            actual_type = os.path.splitext(file)[1].upper()

            # Check if the file has a valid extension
            if actual_type:
                # If the file type is not already in the list, create a new directory
                if actual_type not in types:
                    new_dir = os.path.join(dir, 'Arquivos '+ actual_type)
                    if not os.path.exists(new_dir):
                        try:
                            os.makedirs(new_dir)
                        except OSError as error:
                            raise OSError(f'{error}: {new_dir}')

                    # Move the file to the new directory and add the file type to the list
                    try:
                        shutil.move(os.path.join(dir, file), os.path.join(new_dir, file))
                        types.append(actual_type)
                    except OSError as error:
                        w.warn(f'{error}: {file}\n{types}')
                else:
                    # If the file type is already in the list, move the file to the existing directory
                    new_dir = os.path.join(dir, 'Arquivos '+ actual_type)
                    try:
                        shutil.move(os.path.join(dir, file), os.path.join(new_dir, file))
                    except OSError as error:
                        w.warn(f'{error}: {file}\n{types}')
        return len(types)
        
    def run(self) -> None:
        MainScreen().open_window()

if __name__ == '__main__':
    Main().run()