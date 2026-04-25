# Galz Games — Site do RetroGamerDay

Este repositório contém o site do evento RetroGamerDay organizado pela equipe Galz Games. Inclui páginas estáticas, recursos de mídia e scripts para gerar legendas automáticas e versões com legendas embutidas.

## Estrutura principal
- `index.html` — Página principal do site
- `index.css` — Estilos do site
- `videos/entrevista.mp4` — Vídeo original da entrevista
- `videos/entrevista.vtt` — Legendas geradas (WebVTT)
- `videos/entrevista_hard.mp4` — Vídeo com legendas embutidas (hardcoded)
- `scripts/transcribe_whisper.py` — Script para gerar `entrevista.vtt` usando Whisper
- `ffmpeg/` — binários ffmpeg baixados (usado para processar vídeo)

## Como rodar localmente (rápido)
1. Instale Python 3.8+.
2. (Opcional) Crie e ative um ambiente virtual.
3. Instale dependências para transcrição (se for usar):

```bash
pip install -r requirements.txt
# ou, caso não exista requirements.txt:
pip install openai-whisper ffmpeg-python
```

4. Se não tiver `ffmpeg` no sistema, coloque o binário em `ffmpeg/` (já incluído no repositório durante desenvolvimento) ou instale via pacote do SO.

5. Servir o site localmente (teste rápido):

```bash
python -m http.server 8000 --bind 127.0.0.1
# abra http://127.0.0.1:8000/index.html
```

## Gerar legendas automáticas (WebVTT)
O script `scripts/transcribe_whisper.py` gera `videos/entrevista.vtt` a partir de `videos/entrevista.mp4`:

```bash
# garanta que ffmpeg esteja no PATH ou presente em ./ffmpeg/bin
python scripts/transcribe_whisper.py
```

O script usa o modelo `small` do Whisper. Para melhor precisão, pode usar modelos maiores (requere mais RAM/CPU).

## Gerar vídeo com legendas embutidas (hardcoded)
Com `ffmpeg` disponível, o comando usado para gerar `videos/entrevista_hard.mp4` foi similar a:

```bash
ffmpeg -i "videos/entrevista.mp4" -vf "subtitles=videos/entrevista.vtt:force_style='FontName=Arial,Fontsize=28,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,BackColour=&H80000000'" -c:a copy "videos/entrevista_hard.mp4"
```

Ajuste `Fontsize`/cores conforme desejado e re-encode para atualizar o arquivo hardcoded.

## Observações
- As legendas geradas automaticamente podem conter erros; revise o arquivo `videos/entrevista.vtt` e corrija manualmente se necessário.
- Embutir legendas (hardcoded) facilita a exibição em navegadores e redes sociais que não suportam WebVTT.

## Contribuições
Pull requests são bem-vindos. Para alterações grandes, abra uma issue primeiro.

## Licença
Adicione a licença que preferir antes de publicar o repositório (ex.: MIT).

---
Arquivo atualizado automaticamente via script do projeto. Se quiser que eu adicione instruções extras ou traduções, me avise.
