<div align="center">
  <img src="https://imgur.com/Z2DznGX.png" alt="OrgArq Logo" width="300px"/>
  
  # 📂 Organizador de Arquivos

  *Uma ferramenta simples e eficiente para organizar automaticamente seus arquivos direto pelo Windows.*

  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
    <img alt="PySimpleGUI" src="https://img.shields.io/badge/PySimpleGUI-4.x-green?style=for-the-badge">
  </p>
  
  <p>
    <a href="https://github.com/srkrash/Organizador-de-Arquivos">
      <img src="https://img.shields.io/github/languages/count/srkrash/Organizador-de-Arquivos?style=flat-square">
    </a>
    <a href="https://github.com/srkrash/Organizador-de-Arquivos/commits/main">
      <img src="https://img.shields.io/github/last-commit/srkrash/Organizador-de-Arquivos?style=flat-square">
    </a>
  </p>
</div>

---

## 📖 Sobre o Projeto
O **Organizador de Arquivos** é uma ferramenta com interface gráfica super amigável que arruma a bagunça dos seus diretórios em questão de instantes.

Ao selecionar uma pasta, o programa lê o conteúdo e agrupa os arquivos automaticamente nas categorias abaixo:

| 📂 Categoria | 📄 Extensões Suportadas |
|-------------|----------------------------|
| **Imagens** | `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.tiff`, `.webp`, `.svg` |
| **Áudios** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a` |
| **Vídeos** | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`, `.mpeg` |
| **Documentos** | `.txt`, `.xlsx`, `.xls`, `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx`, `.rtf`, `.csv` |
| **Arquivos e Instaladores** | `.exe`, `.msi`, `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.pkg`, `.deb`, `.rpm`, `.iso` |
| **Outros** | Qualquer outra extensão não mapeada |

<br/>

## 🚀 Como Funciona?

1. Abra o aplicativo.
2. Na interface principal, clique em **Selecionar** e escolha o diretório que deseja organizar.
3. Clique no botão **Organizar**.
4. Uma mensagem aparecerá informando quantas categorias de arquivos foram organizadas!

> **Preview da Tela:** <br/>
> <img alt="Janela do Organizador de Arquivos" src="https://i.imgur.com/gQhiN3o.png" width="400"/>

---

## ⚙️ Dependências

O projeto utiliza a biblioteca **[PySimpleGUI](https://pypi.org/project/PySimpleGUI/)** para construir a janela do aplicativo.

Para instalar as dependências manualmente e rodar o projeto a partir do código fonte:

```bash
pip install PySimpleGUI
```

Em seguida, execute o arquivo principal:
```bash
python main.py
```

---

## ⚡ Executável (Windows)
Se você estiver utilizando a versão convertida em `.exe`, basta executar o `OrgArq.exe`.

> ⚠️ **Atenção:** Em alguns casos, seu software antivírus pode tratar programas empacotados pelo gerador de executáveis do Python (como o PyInstaller) como falso-positivos, movendo seu executável para a quarentena. Caso isso ocorra, adicione o diretório/arquivo na lista de exclusão do seu antivírus.
