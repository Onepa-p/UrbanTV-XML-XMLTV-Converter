# UrbanTV XML → XMLTV Converter

Este projeto converte automaticamente o arquivo XML da UrbanTV para o formato padrão **XMLTV**, compatível com servidores de IPTV, players e apps.

---

 Estrutura do Projeto

```plaintext
urbantv_xmltv/
├── build/                            # Pasta gerada pelo PyInstaller
├── dist/
│   ├── converter_urbantv.exe         # Executável Windows (sem precisar de Python)
│   └── Otaku_XMLTV.xml               # Arquivo XMLTV gerado (se rodar pelo .exe)
├── converter_urbantv.py              # Script principal (Python)
├── converter_urbantv.exe             # Outra cópia do .exe na raiz
├── converter_urbantv.spec            # Arquivo de build do PyInstaller
├── Otaku_XMLTV.xml                   # XMLTV gerado (se rodar via script Python)
├── verificar_duracao.py             # Script opcional que detecta programas longos
└── README.md                         # Este manual


Opção 1: Rodar com Python
Se você tiver Python instalado, siga os passos abaixo:

Abrir o terminal (CMD ou PowerShell):

cd C:\Users\DIRECTORIO\DO ARQUIVO\urbantv_xmltv
Executar o script:
python converter_urbantv.py
Isso criará (ou atualizará) o arquivo Otaku_XMLTV.xml na mesma pasta.

Rodar o executável no Windows
Se não tiver Python instalado, use o .exe:

Entre na pasta onde está o executável:
cd C:\Users\SEU\DIRECTORIO\urbantv_xmltv\dist\converter_urbantv
Rode o programa com duplo clique em:
converter_urbantv.exe

O arquivo Otaku_XMLTV.xml será gerado dentro da mesma pasta dist/.

Verificar programas longos (opcional)
Para identificar programas com duração superior a 4 horas:

Abra o terminal:
cd C:\Users\DIRECTORIO\DO-ARQUIVO\urbantv_xmltv
Execute:

python verificar_duracao.py
Ele mostrará os títulos longos e os horários de início/fim.