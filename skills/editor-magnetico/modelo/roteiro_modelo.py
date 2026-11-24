#!/usr/bin/env python3
"""Roteiro de edição deste projeto (gerado pelo Constancy Editor).
O Claude edita este arquivo e roda:  python3 roteiro.py
Depois:  python3 <motor>/mixar.py .  e  python3 <motor>/renderizar.py . checar|quadros|final
"""
import json, sys
sys.path.insert(0, "%MOTOR%")
from cenas_base import tema, escrever, palavras, dur_video, perfil, ranking

T = tema("%ESTILO%")                  # estilo escolhido no catálogo (01–17)
W = palavras()                        # palavras da fala na linha do tempo final (depois do montar.py)
VDUR = dur_video()
FIM = round(VDUR + 1.5, 2)            # +1,5 s para o encerramento (logo/@/CTA)
INICIO = 0.0                          # React: tempo em que acaba o trecho original que não deve ser mexido

# id: (início, fim, tipo)   p = tela dividida · f = tela cheia com texto · m = motion puro (vídeo some)
CENAS = {
    "c01": (0.0, 3.0, "f"),
}

S = {}

# ---------- c01 · gancho ----------
S["c01"] = dict(css="""
    #c01-h { top: 330px; font-size: 110px; }
""", body="""
    <div id="c01-h" class="t luz">headline <span class="it">aqui</span></div>
""", js="""
    IN("#c01-h", 0.05, { scale: 1.3 });
    OUT("#c01-h", 2.7);
""")

# zoom rápido no rosto em palavras fortes (só vale em tela cheia)
PUNCH = []

# correções de transcrição para a legenda: {"palavra errada": "certa"}
CORRECOES = {}

# efeitos sonoros: 1 por evento visual (apelidos em mixar.py → SONS)
CUES = [
    {"t": 0.05, "som": "impacto-suave", "vol": 0.35},
]

escrever(CENAS, S, T, W, FIM, VDUR, punch=PUNCH, inicio_legendas=INICIO, correcoes=CORRECOES)
json.dump(CUES, open("audio/cues.json", "w"), indent=1)
