import json, math

# Bilingual data
L = {
    "en": {
        "title": "Interactive Tree of Life",
        "tab_seph": "Sephirot",
        "tab_paths": "Paths & Tarot",
        "tab_alch": "Alchemy",
        "btn_show_all": "Show All Labels",
        "btn_hide_all": "Hide All Labels",
        "btn_clear": "Clear Selection",
        "btn_sys_gd": "Golden Dawn",
        "btn_sys_th": "Thelema",

        "th_sephirot": "Sephirot",
        "th_planet": "Planet",
        "th_type": "Type",
        "th_attr": "Attribution",

        "th_element": "Element",
        "th_metal": "Metal",
        "th_num": "#",
        "th_letter": "Letter",
        "th_tarot": "Tarot",
        "th_zodiac": "Zodiac",
        "th_alchemy": "Alchemy",
        "info_connects": "Connects",
        "info_tarot": "Tarot",
        "info_planet": "Planetary",
        "info_type": "Type",
        "info_attr": "Attribution",

        "info_zodiac": "Zodiac",
        "info_alchem": "Alchemical",
        "info_planet_s": "Planet / Influence",
        "info_metal": "Alchemical Metal",
        "alch_title": "The Alchemical Great Work",
        "alch_meaning": "Meaning",
        "alch_use": "Symbolic Use",
        "tria_title": "Tria Prima \u2014 The Three Primes",
        "tria_desc": "Sulfur, Mercury, and Salt together are the three essential principles of creation and transformation:",
        "tria_s": "\U0001f70d Sulfur \u2014 the soul, the active principle",
        "tria_m": "\u263f Mercury \u2014 the spirit, the volatile principle",
        "tria_sa": "\U0001f714 Salt \u2014 the body, the stabilizing principle",
    },
    "pt": {
        "title": "\xc1rvore da Vida Interativa",
        "tab_seph": "Sefirot",
        "tab_paths": "Caminhos & Tarot",
        "tab_alch": "Alquimia",
        "btn_show_all": "Mostrar Todos os R\xf3tulos",
        "btn_hide_all": "Esconder R\xf3tulos",
        "btn_clear": "Limpar Sele\xe7\xe3o",
        "btn_sys_gd": "Golden Dawn",
        "btn_sys_th": "Thelema",

        "th_sephirot": "Sefirot",
        "th_planet": "Planeta",
        "th_type": "Tipo",
        "th_attr": "Atribui\xe7\xe3o",

        "th_element": "Elemento",
        "th_metal": "Metal",
        "th_num": "#",
        "th_letter": "Letra",
        "th_tarot": "Tarot",
        "th_zodiac": "Zod\xedaco",
        "th_alchemy": "Alquimia",
        "info_connects": "Conecta",
        "info_tarot": "Tarot",
        "info_planet": "Planet\xe1rio",
        "info_type": "Tipo",
        "info_attr": "Atribui\xe7\xe3o",

        "info_zodiac": "Zod\xedaco",
        "info_alchem": "Alqu\xedmico",
        "info_planet_s": "Planeta / Influ\xeancia",
        "info_metal": "Metal Alqu\xedmico",
        "alch_title": "A Grande Obra Alqu\xedmica",
        "alch_meaning": "Significado",
        "alch_use": "Uso Simb\xf3lico",
        "tria_title": "Tria Prima \u2014 Os Tr\xeas Primeiros",
        "tria_desc": "Enxofre, Merc\xfario e Sal s\xe3o juntos os tr\xeas princ\xedpios essenciais da cria\xe7\xe3o e transforma\xe7\xe3o:",
        "tria_s": "\U0001f70d Enxofre \u2014 a alma, o princ\xedpio ativo",
        "tria_m": "\u263f Merc\xfario \u2014 o esp\xedrito, o princ\xedpio vol\xe1til",
        "tria_sa": "\U0001f714 Sal \u2014 o corpo, o princ\xedpio estabilizador",
    }
}

spheres = {
    "Keter":     (400, 100,  "#fff5cc", "#daa520", "\U0001f772", {"en": "Keter",     "pt": "Keter"}),
    "Chokmah":   (600, 250,  "#cce5ff", "#1e90ff", "\u2605",     {"en": "Chokmah",  "pt": "Chokmah"}),
    "Binah":     (200, 250,  "#fcdada", "#800000", "\u2644",     {"en": "Binah",     "pt": "Binah"}),
    "Chesed":    (600, 550,  "#99ccff", "#1e90ff", "\u2643",     {"en": "Chesed",    "pt": "Chesed"}),
    "Geburah":   (200, 550,  "#fcbcbc", "#800000", "\u2642",     {"en": "Geburah",   "pt": "Geburah"}),
    "Tiphareth": (400, 700,  "#fff0a5", "#daa520", "\u2609",     {"en": "Tiphareth", "pt": "Tiphareth"}),
    "Netzach":   (600, 850,  "#66b3ff", "#1e90ff", "\u2640",     {"en": "Netzach",   "pt": "Netzach"}),
    "Hod":       (200, 850,  "#fca5a5", "#800000", "\u263f",     {"en": "Hod",       "pt": "Hod"}),
    "Yesod":     (400, 1000, "#ffe680", "#daa520", "\u263d",     {"en": "Yesod",     "pt": "Yesod"}),
    "Malkuth":   (400, 1150, "#ffd700", "#daa520", "\u2641",     {"en": "Malkuth",   "pt": "Malkuth"}),
}

# tarot_name: {en, pt}
paths = [
    (0,  "Aleph",  "א", "Keter",     "Chokmah",   "0",    {"en":"The Fool",          "pt":"O Louco"},          "0",    {"en":"The Fool",          "pt":"O Louco"},          0.5,  1,  -1,   45, {"en":"Element", "pt":"Elemento"}, {"en":"🜁 Air", "pt":"🜁 Ar"}),
    (1,  "Beth",   "ב", "Keter",     "Binah",     "I",    {"en":"The Magician",      "pt":"O Mago"},           "I",    {"en":"The Magician",      "pt":"O Mago"},           0.5,  -1, -1,   45, {"en":"Planet", "pt":"Planeta"}, {"en":"☿ Mercury", "pt":"☿ Mercúrio"}),
    (2,  "Gimel",  "ג", "Keter",     "Tiphareth", "II",   {"en":"High Priestess",    "pt":"A Sacerdotisa"},    "II",   {"en":"High Priestess",    "pt":"A Sacerdotisa"},    0.3,  1,  0,    50, {"en":"Planet", "pt":"Planeta"}, {"en":"☽ Moon", "pt":"☽ Lua"}),
    (3,  "Daleth", "ד", "Binah",     "Chokmah",   "III",  {"en":"The Empress",       "pt":"A Imperatriz"},     "III",  {"en":"The Empress",       "pt":"A Imperatriz"},     0.5,  0,  -1,   45, {"en":"Planet", "pt":"Planeta"}, {"en":"♀ Venus", "pt":"♀ Vênus"}),
    (4,  "He",     "ה", "Chokmah",   "Chesed",    "IV",   {"en":"The Emperor",       "pt":"O Imperador"},      "XVII", {"en":"The Star",          "pt":"A Estrela"},        0.5,  1,  0,    55, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♈ Aries", "pt":"♈ Áries"}),
    (5,  "Vav",    "ו", "Chokmah",   "Tiphareth", "V",    {"en":"The Hierophant",    "pt":"O Hierofante"},     "V",    {"en":"The Hierophant",    "pt":"O Hierofante"},     0.45, 1,  -0.6, 60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♉ Taurus", "pt":"♉ Touro"}),
    (6,  "Zayin",  "ז", "Binah",     "Tiphareth", "VI",   {"en":"The Lovers",        "pt":"Os Amantes"},       "VI",   {"en":"The Lovers",        "pt":"Os Amantes"},       0.45, -1, -0.6, 60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♊ Gemini", "pt":"♊ Gêmeos"}),
    (7,  "Cheth",  "ח", "Binah",     "Geburah",   "VII",  {"en":"The Chariot",       "pt":"O Carro"},          "VII",  {"en":"The Chariot",       "pt":"O Carro"},          0.5,  -1, 0,    55, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♋ Cancer", "pt":"♋ Câncer"}),
    (8,  "Teth",   "ט", "Geburah",   "Chesed",    "VIII", {"en":"Strength",          "pt":"Força"},            "VIII", {"en":"Strength",          "pt":"Força"},            0.5,  0,  -1,   40, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♌ Leo", "pt":"♌ Leão"}),
    (9,  "Yod",    "י", "Chesed",    "Tiphareth", "IX",   {"en":"The Hermit",        "pt":"O Eremita"},        "IX",   {"en":"The Hermit",        "pt":"O Eremita"},        0.55, 1,  0.6,  60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♍ Virgo", "pt":"♍ Virgem"}),
    (10, "Kaph",   "כ", "Chesed",    "Netzach",   "X",    {"en":"Wheel of Fortune",  "pt":"A Roda da Fortuna"}, "X",   {"en":"Wheel of Fortune",  "pt":"A Roda da Fortuna"}, 0.5, 1,  0,    55, {"en":"Planet", "pt":"Planeta"}, {"en":"♃ Jupiter", "pt":"♃ Júpiter"}),
    (11, "Lamed",  "ל", "Geburah",   "Tiphareth", "XI",   {"en":"Justice",           "pt":"Justiça"},          "XI",   {"en":"Justice",           "pt":"Justiça"},          0.55, -1, 0.6,  60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♎ Libra", "pt":"♎ Libra"}),
    (12, "Mem",    "מ", "Geburah",   "Hod",       "XII",  {"en":"The Hanged Man",    "pt":"O Enforcado"},      "XII",  {"en":"The Hanged Man",    "pt":"O Enforcado"},      0.5,  -1, 0,    55, {"en":"Element", "pt":"Elemento"}, {"en":"🜄 Water", "pt":"🜄 Água"}),
    (13, "Nun",    "נ", "Tiphareth", "Netzach",   "XIII", {"en":"Death",             "pt":"A Morte"},          "XIII", {"en":"Death",             "pt":"A Morte"},          0.5,  1,  -0.6, 60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♏ Scorpio", "pt":"♏ Escorpião"}),
    (14, "Samekh", "ס", "Tiphareth", "Yesod",     "XIV",  {"en":"Temperance",        "pt":"Temperança"},       "XIV",  {"en":"Temperance",        "pt":"Temperança"},       0.3,  -1, 0,    50, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♐ Sagittarius", "pt":"♐ Sagitário"}),
    (15, "Ayin",   "ע", "Tiphareth", "Hod",       "XV",   {"en":"The Devil",         "pt":"O Diabo"},          "XV",   {"en":"The Devil",         "pt":"O Diabo"},          0.5,  -1, -0.6, 60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♑ Capricorn", "pt":"♑ Capricórnio"}),
    (16, "Pe",     "פ", "Hod",       "Netzach",   "XVI",  {"en":"The Tower",         "pt":"A Torre"},          "XVI",  {"en":"The Tower",         "pt":"A Torre"},          0.5,  0,  1,    45, {"en":"Planet", "pt":"Planeta"}, {"en":"♂ Mars", "pt":"♂ Marte"}),
    (17, "Tzaddi", "צ", "Netzach",   "Yesod",     "XVII", {"en":"The Star",          "pt":"A Estrela"},        "IV",   {"en":"The Emperor",       "pt":"O Imperador"},      0.55, 1,  0.6,  60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♒ Aquarius", "pt":"♒ Aquário"}),
    (18, "Qoph",   "ק", "Hod",       "Yesod",     "XVIII",{"en":"The Moon",          "pt":"A Lua"},            "XVIII",{"en":"The Moon",          "pt":"A Lua"},            0.55, -1, 0.6,  60, {"en":"Zodiac", "pt":"Zodíaco"}, {"en":"♓ Pisces", "pt":"♓ Peixes"}),
    (19, "Resh",   "ר", "Yesod",     "Malkuth",   "XIX",  {"en":"The Sun",           "pt":"O Sol"},            "XIX",  {"en":"The Sun",           "pt":"O Sol"},            0.5,  1,  0,    50, {"en":"Planet", "pt":"Planeta"}, {"en":"☉ Sun", "pt":"☉ Sol"}),
    (20, "Shin",   "ש", "Netzach",   "Malkuth",   "XX",   {"en":"Judgement",         "pt":"Julgamento"},       "XX",   {"en":"The Aeon",          "pt":"O Aeon"},           0.65, 1,  0.5,  65, {"en":"Element", "pt":"Elemento"}, {"en":"🜂 Fire", "pt":"🜂 Fogo"}),
    (21, "Tav",    "ת", "Hod",       "Malkuth",   "XXI",  {"en":"The World",         "pt":"O Mundo"},          "XXI",  {"en":"The Universe",      "pt":"O Universo"},       0.65, -1, 0.5,  65, {"en":"Planet", "pt":"Planeta"}, {"en":"♄ Saturn", "pt":"♄ Saturno"}),
]

sefirot_data = [
    ("Keter",     {"en":"Keter",          "pt":"Keter"},          {"en":"Divine / None",     "pt":"Divino / Nenhum"}, {"en":"Spirit",         "pt":"Espírito"},        {"en":"None",            "pt":"Nenhum"}),
    ("Chokmah",   {"en":"Chokmah",        "pt":"Chokmah"},        {"en":"Zodiac / Stars",    "pt":"Zodíaco / Estrelas"},{"en":"Fire",           "pt":"Fogo"},               {"en":"None",            "pt":"Nenhum"}),
    ("Binah",     {"en":"Binah",          "pt":"Binah"},          {"en":"♄ Saturn",      "pt":"♄ Saturno"},   {"en":"Earth / Water",  "pt":"Terra / Água"},    {"en":"Lead (♄)",   "pt":"Chumbo (♄)"}),
    ("Daat",      {"en":"Da'at",          "pt":"Da'at"},          {"en":"None",               "pt":"Nenhum"},           {"en":"Knowledge / Void","pt":"Conhecimento / Vazio"},{"en":"None",           "pt":"Nenhum"}),
    ("Chesed",    {"en":"Chesed",         "pt":"Chesed"},         {"en":"♃ Jupiter",     "pt":"♃ Júpiter"},{"en":"Water",          "pt":"Água"},             {"en":"Tin (♃)",    "pt":"Estanho (♃)"}),
    ("Geburah",   {"en":"Geburah",        "pt":"Geburah"},        {"en":"♂ Mars",        "pt":"♂ Marte"},     {"en":"Fire",           "pt":"Fogo"},               {"en":"Iron (♂)",   "pt":"Ferro (♂)"}),
    ("Tiphareth", {"en":"Tiphareth",      "pt":"Tiphareth"},      {"en":"☉ Sun",         "pt":"☉ Sol"},       {"en":"Fire / Harmony", "pt":"Fogo / Harmonia"},    {"en":"Gold (☉)",   "pt":"Ouro (☉)"}),
    ("Netzach",   {"en":"Netzach",        "pt":"Netzach"},        {"en":"♀ Venus",       "pt":"♀ Vênus"},  {"en":"Earth / Water",  "pt":"Terra / Água"},    {"en":"Copper (♀)", "pt":"Cobre (♀)"}),
    ("Hod",       {"en":"Hod",            "pt":"Hod"},            {"en":"☿ Mercury",     "pt":"☿ Mercúrio"},{"en":"Air",            "pt":"Ar"},                 {"en":"Mercury (☿)","pt":"Mercúrio (☿)"}),
    ("Yesod",     {"en":"Yesod",          "pt":"Yesod"},          {"en":"☽ Moon",        "pt":"☽ Lua"},       {"en":"Water",          "pt":"Água"},             {"en":"Silver (☽)", "pt":"Prata (☽)"}),
    ("Malkuth",   {"en":"Malkuth",        "pt":"Malkuth"},        {"en":"Earth",             "pt":"Terra"},           {"en":"Earth",          "pt":"Terra"},              {"en":"None",            "pt":"Nenhum"}),
]

# Build JS data: bilingual
js_seph = {}
for key, name_bi, planet_bi, element_bi, metal_bi in sefirot_data:
    js_seph[key] = {"name": name_bi, "planet": planet_bi, "element": element_bi, "metal": metal_bi}

js_paths = {}
for pid, letter, heb, s1, s2, tarot_gd_num, tarot_gd_bi, tarot_th_num, tarot_th_bi, t, nx, ny, dist, attr_type_bi, attr_val_bi in paths:
    js_paths[str(pid)] = {
        "id": pid, "letter": letter, "heb": heb,
        "s1": s1, "s2": s2,
        "tarot_gd_num": tarot_gd_num, "tarot_gd_name": tarot_gd_bi,
        "tarot_th_num": tarot_th_num, "tarot_th_name": tarot_th_bi,
        "attr_type": attr_type_bi, "attr_val": attr_val_bi
    }

# alch blocks bilingual: (sym, title_en, title_pt, meaning_en, meaning_pt, use_en, use_pt)
alch_blocks = [
    ("\U0001f702",
     "Fire", "Fogo",
     "Fire is associated with spirit, transformation, and energy \u2014 the active, masculine principle. It represents the intense heat that purifies.",
     "O Fogo est\xe1 associado ao esp\xedrito, transforma\xe7\xe3o e energia \u2014 o princ\xedpio ativo e masculino. Representa o calor intenso que purifica.",
     "Fire breaks down material substances (calcination) and purifies them, symbolizing the soul\u2019s journey through trials to enlightenment.",
     "O Fogo decompõe subst\xe2ncias materiais (calcina\xe7\xe3o) e as purifica, simbolizando a jornada da alma atrav\xe9s das provações rumo \xe0 ilumina\xe7\xe3o."),
    ("\U0001f704",
     "Water", "\xc1gua",
     "Water is the passive, feminine principle \u2014 emotion, intuition, and the unconscious. It represents fluidity, fertility, and nourishment.",
     "A \xc1gua \xe9 o princ\xedpio passivo e feminino \u2014 emo\xe7\xe3o, intui\xe7\xe3o e o inconsciente. Representa fluidez, fertilidade e nutri\xe7\xe3o.",
     "In alchemy, Water represents dissolution: breaking down rigid structures to allow adaptation and transformation.",
     "Na alquimia, a \xc1gua representa a dissolu\xe7\xe3o: a decomposi\xe7\xe3o de estruturas r\xedgidas para permitir a adapta\xe7\xe3o e transforma\xe7\xe3o."),
    ("\U0001f701",
     "Air", "Ar",
     "Air stands for intellect, communication, and the breath of life \u2014 mental activity, thought, rationality, movement, and freedom.",
     "O Ar representa o intelecto, comunica\xe7\xe3o e o sopro da vida \u2014 atividade mental, pensamento, racionalidade e liberdade.",
     "Air symbolizes transformation through intellectual insight, relating to evaporation, where volatile elements are extracted and purified.",
     "O Ar simboliza a transforma\xe7\xe3o atrav\xe9s da clareza intelectual, relacionando-se \xe0 evapora\xe7\xe3o, onde elementos vol\xe1teis são extra\xeddos e purificados."),
    ("\U0001f703",
     "Earth", "Terra",
     "Earth represents matter, stability, and the physical body \u2014 the foundation for the work of transformation.",
     "A Terra representa a mat\xe9ria, estabilidade e o corpo f\xedsico \u2014 a funda\xe7\xe3o para a obra de transforma\xe7\xe3o.",
     "Earth is the starting point: the base material that will be purified into something of higher value.",
     "A Terra \xe9 o ponto de partida: o material bruto que ser\xe1 purificado em algo de maior valor."),
    ("\U0001f70d",
     "Sulfur \u2014 The Soul", "Enxofre \u2014 A Alma",
     "Sulfur symbolizes the soul, the active principle, the spark of life \u2014 passion, fire, vitality, and will.",
     "O Enxofre simboliza a alma, o princ\xedpio ativo, a cen\xedlha da vida \u2014 paix\xe3o, fogo, vitalidade e vontade.",
     "Sulfur is the agent of combustion or spiritual fire, fueling the work of transformation and purification.",
     "O Enxofre \xe9 o agente da combust\xe3o ou fogo espiritual, alimentando a obra de transforma\xe7\xe3o e purifica\xe7\xe3o."),
    ("\U0001f714",
     "Salt \u2014 The Body", "Sal \u2014 O Corpo",
     "Salt symbolizes the body and the crystallization of the physical world \u2014 the stabilizing principle of preservation.",
     "O Sal simboliza o corpo e a cristaliza\xe7\xe3o do mundo f\xedsico \u2014 o princ\xedpio estabilizador de preserva\xe7\xe3o.",
     "Salt is associated with coagulation. It is the final product of alchemical work, representing the reunion of spirit and matter.",
     "O Sal est\xe1 associado \xe0 coagula\xe7\xe3o. \xc9 o produto final da obra alqu\xedmica, representando a reuni\xe3o do esp\xedrito com a mat\xe9ria."),
    ("\u263f",
     "Mercury \u2014 The Spirit", "Merc\xfario \u2014 O Esp\xedrito",
     "Mercury represents the spirit, the volatile principle, and the connection between physical and spiritual realms. Fluid, changeable, adaptive.",
     "O Merc\xfario representa o esp\xedrito, o princ\xedpio vol\xe1til e a conex\xe3o entre os reinos f\xedsico e espiritual. Fluido, mut\xe1vel e adaptativo.",
     "Mercury is central to transmutation: it dissolves and transforms substances, carrying the potential for the Philosopher's Stone.",
     "O Merc\xfario \xe9 central na transmuta\xe7\xe3o: dissolve e transforma subst\xe2ncias, carregando o potencial da Pedra Filosofal."),
]

# =========================================================
# GENERATE HTML
# =========================================================
html_lines = []
def W(s): html_lines.append(s)

W("<!DOCTYPE html>")
W('<html lang="en">')
W("<head>")
W('  <meta charset="utf-8">')
W('  <title id="pageTitle">Interactive Tree of Life</title>')
W("  <style>")
W("""
    *, *::before, *::after { box-sizing: border-box; }
    body { font-family: "Segoe UI", Arial, sans-serif; background: #f4f6f9; margin: 0; padding: 0; display: flex; height: 100vh; overflow: hidden; }

    /* TREE SIDE */
    .tree-wrap { flex: 1; min-width: 0; height: 100vh; display: flex; justify-content: center; align-items: center; background: #fff; position: relative; }
    .tree-wrap svg { max-height: 96%; max-width: 96%; height: auto; cursor: default; }

    /* SVG interactions */
    .seph-g { cursor: pointer; }
    .seph-g circle { transition: filter .2s, stroke-width .2s; }
    .seph-g:hover circle { filter: drop-shadow(0 0 10px rgba(52,152,219,.8)); stroke-width: 6; }
    .seph-g.selected circle { filter: drop-shadow(0 0 14px rgba(41,128,185,1)); stroke-width: 7; stroke: #2980b9 !important; }
    .path-g { cursor: pointer; }
    .path-g .vis-line { transition: stroke .18s, stroke-width .18s; }
    .path-g:hover .vis-line { stroke: #e74c3c; stroke-width: 8; }
    .path-g.selected .vis-line { stroke: #f39c12; stroke-width: 7; }
    .path-label { transition: opacity .22s ease, transform .22s ease; }

    /* FLOATING INFO - bottom left of tree area */
    #infoPanel {
      position: absolute; bottom: 18px; left: 18px;
      background: rgba(255,255,255,.97); border-radius: 12px;
      padding: 15px 22px; min-width: 260px; max-width: 380px;
      box-shadow: 0 6px 24px rgba(0,0,0,.13); border-left: 5px solid #3498db;
      display: none; z-index: 200; font-size: 14px; line-height: 1.5;
    }
    #infoPanel h3 { margin: 0 0 8px; color: #2c3e50; font-size: 16px; }
    .info-row { display: flex; justify-content: space-between; gap: 10px; border-bottom: 1px solid #f0f0f0; padding: 4px 0; font-size: 13px; }
    .info-label { font-weight: 600; color: #7f8c8d; white-space: nowrap; }
    .sym { font-family: "Segoe UI Symbol", sans-serif; }

    /* TREE TOOLBAR */
    .tree-toolbar { position: absolute; top: 12px; right: 12px; display: flex; flex-direction: column; gap: 7px; z-index: 100; }
    .tree-toolbar button { background: #2c3e50; color: #fff; border: none; padding: 8px 13px; border-radius: 8px; cursor: pointer; font-size: 12px; font-weight: bold; box-shadow: 0 2px 6px rgba(0,0,0,.15); transition: background .18s; }
    .tree-toolbar button:hover { background: #34495e; }
    .tree-toolbar button.active { background: #c0392b; }
    
    /* LANG/SYS TOGGLES */
    .lang-toggle, .sys-toggle { display: flex; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,.15); }
    .lang-toggle button, .sys-toggle button { margin: 0; border-radius: 0; box-shadow: none; background: #34495e; color: #95a5a6; flex: 1; padding: 8px 10px; border-bottom: 3px solid transparent; }
    .lang-toggle button:hover, .sys-toggle button:hover { background: #2c3e50; color: #fff; }
    .lang-toggle button.active, .sys-toggle button.active { background: #2c3e50; color: #1abc9c; border-bottom-color: #1abc9c; }

    /* PANEL */
    .panel { width: 48vw; height: 100vh; background: #f4f6f9; display: flex; flex-direction: column; box-shadow: -4px 0 15px rgba(0,0,0,.07); position: relative; transition: width .4s cubic-bezier(0.25, 0.8, 0.25, 1); flex-shrink: 0; }
    .panel-inner { width: 48vw; height: 100vh; display: flex; flex-direction: column; overflow: hidden; opacity: 1; transition: opacity .2s ease; }
    .panel.closed { width: 0 !important; }
    .panel.closed .panel-inner { opacity: 0; pointer-events: none; }
    .dock-btn { position: absolute; left: -38px; top: 50%; transform: translateY(-50%); width: 38px; height: 72px; background: #2c3e50; color: #fff; border: none; border-radius: 8px 0 0 8px; cursor: pointer; font-size: 18px; z-index: 50; box-shadow: -2px 0 6px rgba(0,0,0,.15); transition: background .18s; }
    .dock-btn:hover { background: #34495e; }

    /* TABS */
    .tabs-bar { display: flex; background: #2c3e50; overflow-x: auto; flex-shrink: 0; }
    .tab-btn { background: transparent; border: none; color: #95a5a6; padding: 14px 17px; font-size: 13px; font-weight: 700; cursor: pointer; border-bottom: 3px solid transparent; white-space: nowrap; transition: color .18s; }
    .tab-btn:hover { color: #fff; }
    .tab-btn.active { color: #fff; border-bottom-color: #3498db; }
    .tab-pane { display: none; flex: 1; overflow-y: auto; padding: 20px; }
    .tab-pane.active { display: block; }

    /* TABLES */
    .tbl-box { background: #fff; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,.06); overflow: hidden; margin-bottom: 22px; }
    table { width: 100%; border-collapse: collapse; }
    th { background: #34495e; color: #fff; padding: 10px 13px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: .5px; }
    td { padding: 8px 13px; border-bottom: 1px solid #eee; font-size: 13px; color: #333; }
    tbody tr:nth-child(even) { background: #f8f9fa; }
    tbody tr:hover { background: #e3e8ef; cursor: pointer; }
    .c-red { font-weight: 700; color: #e74c3c; }
    .c-teal { font-weight: 500; color: #16a085; }
    .c-grey { font-weight: 700; color: #7f8c8d; }

    /* ALCHEMY */
    .alch-card { background: #fff; border-radius: 10px; padding: 20px 24px; box-shadow: 0 2px 8px rgba(0,0,0,.06); margin-bottom: 20px; }
    .alch-card h2 { margin: 0 0 14px; color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 7px; font-size: 18px; }
    .alch-block { margin-bottom: 18px; }
    .alch-title { font-size: 15px; font-weight: 700; color: #e67e22; display: flex; align-items: center; gap: 7px; margin-bottom: 5px; }
    .alch-title .s { font-family: "Segoe UI Symbol", sans-serif; font-size: 20px; }
    .alch-text { font-size: 13.5px; color: #444; line-height: 1.65; margin-bottom: 7px; }
""")
W("  </style>")
W("</head>")
W("<body>")

# ---- TREE ----
W('<div class="tree-wrap" id="treeWrap" onclick="handleBgClick(event)">')
W('  <div class="tree-toolbar">')
W('    <div class="lang-toggle">')
W('      <button id="btnLangEN" class="active" onclick="setLang(event, \'en\')">EN-US</button>')
W('      <button id="btnLangPT" onclick="setLang(event, \'pt\')">PT-BR</button>')
W('    </div>')
W('    <div class="sys-toggle">')
W('      <button id="btnSysGD" class="active" onclick="setSys(event, \'gd\')" data-en="Golden Dawn" data-pt="Golden Dawn">Golden Dawn</button>')
W('      <button id="btnSysTH" onclick="setSys(event, \'th\')" data-en="Thelema" data-pt="Thelema">Thelema</button>')
W('    </div>')
W('    <button id="btnToggleAll" onclick="toggleAllLabels(event)" data-en="Show All Labels" data-pt="Mostrar Todos">Show All Labels</button>')
W('    <button id="btnClear" onclick="clearSelection(event)" data-en="Clear Selection" data-pt="Limpar Sele\xe7\xe3o">Clear Selection</button>')
W("  </div>")
W('  <div id="infoPanel"></div>')
W('  <svg id="treeSvg" viewBox="0 0 800 1250" xmlns="http://www.w3.org/2000/svg" font-family="Arial">')
W("    <defs>")
W('      <filter id="glow"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
W("    </defs>")

# Base faded lines
for pid, letter, heb, s1, s2, tarot_gd_num, tarot_gd_bi, tarot_th_num, tarot_th_bi, t, nx, ny, dist, attr_type_bi, attr_val_bi in paths:
    x1, y1 = spheres[s1][0], spheres[s1][1]
    x2, y2 = spheres[s2][0], spheres[s2][1]
    W(f'    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#ddd" stroke-width="3" />')

W("")

# Clickable paths + labels
for pid, letter, heb, s1, s2, tarot_gd_num, tarot_gd_bi, tarot_th_num, tarot_th_bi, t, nx, ny, dist, attr_type_bi, attr_val_bi in paths:
    x1, y1 = spheres[s1][0], spheres[s1][1]
    x2, y2 = spheres[s2][0], spheres[s2][1]
    mx = x1 + (x2 - x1) * t
    my = y1 + (y2 - y1) * t
    n_len = math.sqrt(nx*nx + ny*ny)
    if n_len: nx2, ny2 = nx/n_len, ny/n_len
    else: nx2, ny2 = 1, 0
    lx = mx + nx2 * (dist + 10)
    ly = my + ny2 * (dist + 10)
    bw = 96 if len(letter) >= 6 else 86
    bh = 50  # taller for 3 lines

    en_gd = tarot_gd_bi["en"]
    pt_gd = tarot_gd_bi["pt"]
    en_th = tarot_th_bi["en"]
    pt_th = tarot_th_bi["pt"]

    W(f'    <g id="path_{pid}" class="path-g" onclick="selectPath(event,{pid})">')
    W(f'      <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="transparent" stroke-width="22" />')
    W(f'      <line class="vis-line" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#666" stroke-width="3" />')
    W(f'    </g>')

    # Label: 3 lines
    W(f'    <g id="label_{pid}" class="path-label" style="opacity:0;pointer-events:none;transform-origin:{lx}px {ly}px;transform:scale(0.85);">')
    W(f'      <line x1="{mx}" y1="{my}" x2="{lx}" y2="{ly}" stroke="#bbb" stroke-width="1.5" stroke-dasharray="4,3" />')
    W(f'      <rect x="{lx-bw/2}" y="{ly-bh/2}" width="{bw}" height="{bh}" rx="10" fill="#fff" stroke="#555" stroke-width="1.5" />')
    W(f'      <text x="{lx}" y="{ly-15}" text-anchor="middle" dominant-baseline="middle" font-weight="bold" font-size="13" fill="#222">{letter} \u2013 {heb}</text>')
    W(f'      <text id="lnum_{pid}" x="{lx}" y="{ly}" text-anchor="middle" dominant-baseline="middle" font-size="12" fill="#777" data-gd="{tarot_gd_num}" data-th="{tarot_th_num}">{tarot_gd_num}</text>')
    W(f'      <text id="lname_{pid}" x="{lx}" y="{ly+14}" text-anchor="middle" dominant-baseline="middle" font-size="12" fill="#444" data-enger="{en_gd}" data-ptger="{pt_gd}" data-enth="{en_th}" data-ptth="{pt_th}">{en_gd}</text>')
    W(f'    </g>')

W("")

# Spheres
for key, (cx, cy, bg, border, sym, name_bi) in spheres.items():
    en_name = name_bi["en"] if isinstance(name_bi, dict) else name_bi
    pt_name = name_bi["pt"] if isinstance(name_bi, dict) else name_bi
    W(f'    <g id="seph_{key}" class="seph-g" onclick="selectSphere(event,\'{key}\')">')
    W(f'      <circle cx="{cx}" cy="{cy}" r="50" fill="{bg}" stroke="{border}" stroke-width="3" />')
    W(f'      <text id="sname_{key}" x="{cx}" y="{cy-13}" text-anchor="middle" dominant-baseline="middle" font-weight="bold" font-size="14" fill="#333" data-en="{en_name}" data-pt="{pt_name}">{en_name}</text>')
    W(f'      <text x="{cx}" y="{cy+14}" text-anchor="middle" dominant-baseline="middle" font-family="\'Segoe UI Symbol\',sans-serif" font-size="26" fill="#333">{sym}</text>')
    W(f'    </g>')

# Da'at
W('    <g id="seph_Daat" class="seph-g" onclick="selectSphere(event,\'Daat\')">')
W('      <circle cx="400" cy="400" r="37" fill="#d1a3ff" stroke="#777" stroke-width="2" stroke-dasharray="7,5" />')
W('      <text id="sname_Daat" x="400" y="400" text-anchor="middle" dominant-baseline="middle" font-style="italic" font-weight="bold" font-size="15" fill="#555" data-en="Da\'at" data-pt="Da\'at">Da\'at</text>')
W('    </g>')

W("  </svg>")
W("</div>")

# ---- PANEL ----
W('<div class="panel" id="sidePanel">')
W('  <button class="dock-btn" id="dockBtn" onclick="togglePanel(event)" title="Toggle panel">&#9654;</button>')
W('  <div class="panel-inner">')
W('  <div class="tabs-bar">')
W('    <button class="tab-btn active" id="tb-seph" onclick="openTab(\'t-seph\',this)">Sephirot</button>')
W('    <button class="tab-btn" id="tb-paths" onclick="openTab(\'t-paths\',this)">Paths &amp; Tarot</button>')
W('    <button class="tab-btn" id="tb-alch" onclick="openTab(\'t-alch\',this)">Alchemy</button>')
W("  </div>")

# TAB: SEPHIROT
W('  <div id="t-seph" class="tab-pane active">')
W('    <div class="tbl-box"><table>')
W('      <thead><tr>')
W('        <th id="th-seph">Sephirot</th>')
W('        <th id="th-planet">Planet</th>')
W('        <th id="th-element">Element</th>')
W('        <th id="th-metal">Metal</th>')
W("      </tr></thead>")
W("      <tbody>")
for key, name_bi, planet_bi, element_bi, metal_bi in sefirot_data:
    en_n = name_bi["en"] if isinstance(name_bi, dict) else name_bi
    pt_n = name_bi["pt"] if isinstance(name_bi, dict) else name_bi
    en_p = planet_bi["en"] if isinstance(planet_bi, dict) else planet_bi
    pt_p = planet_bi["pt"] if isinstance(planet_bi, dict) else planet_bi
    en_e = element_bi["en"] if isinstance(element_bi, dict) else element_bi
    pt_e = element_bi["pt"] if isinstance(element_bi, dict) else element_bi
    en_m = metal_bi["en"] if isinstance(metal_bi, dict) else metal_bi
    pt_m = metal_bi["pt"] if isinstance(metal_bi, dict) else metal_bi
    W(f'      <tr onclick="selectSphere(event,\'{key}\')">')
    W(f'        <td style="font-weight:700" data-en="{en_n}" data-pt="{pt_n}">{en_n}</td>')
    W(f'        <td class="sym" data-en="{en_p}" data-pt="{pt_p}">{en_p}</td>')
    W(f'        <td data-en="{en_e}" data-pt="{pt_e}">{en_e}</td>')
    W(f'        <td class="sym" data-en="{en_m}" data-pt="{pt_m}">{en_m}</td>')
    W("      </tr>")
W("      </tbody></table></div>")
W("  </div>")

# TAB: PATHS
W('  <div id="t-paths" class="tab-pane">')
W('    <div class="tbl-box"><table>')
W('      <thead><tr>')
W('        <th id="th-num">#</th>')
W('        <th id="th-letter">Letter</th>')
W('        <th id="th-tarot">Tarot</th>')
W('        <th id="th-type">Type</th>')
W('        <th id="th-attr">Attribution</th>')
W("      </tr></thead>")
W("      <tbody>")
for pid, letter, heb, s1, s2, tarot_gd_num, tarot_gd_bi, tarot_th_num, tarot_th_bi, t, nx, ny, dist, attr_type_bi, attr_val_bi in paths:
    en_tn_gd = tarot_gd_bi["en"]
    pt_tn_gd = tarot_gd_bi["pt"]
    en_tn_th = tarot_th_bi["en"]
    pt_tn_th = tarot_th_bi["pt"]
    en_type = attr_type_bi["en"]
    pt_type = attr_type_bi["pt"]
    en_attr = attr_val_bi["en"]
    pt_attr = attr_val_bi["pt"]

    W(f'      <tr onclick="selectPath(event,{pid})">')
    W(f'        <td class="c-grey">{pid}</td>')
    W(f'        <td class="c-red">{letter} \u2013 {heb}</td>')
    W(f'        <td class="c-teal" id="tbl_path_tarot_{pid}" data-enger="{tarot_gd_num} | {en_tn_gd}" data-ptger="{tarot_gd_num} | {pt_tn_gd}" data-enth="{tarot_th_num} | {en_tn_th}" data-ptth="{tarot_th_num} | {pt_tn_th}">{tarot_gd_num} | {en_tn_gd}</td>')
    W(f'        <td data-en="{en_type}" data-pt="{pt_type}">{en_type}</td>')
    W(f'        <td class="sym" data-en="{en_attr}" data-pt="{pt_attr}">{en_attr}</td>')
    W("      </tr>")
W("      </tbody></table></div>")
W("  </div>")

# TAB: ALCHEMY
W('  <div id="t-alch" class="tab-pane">')
W('    <div class="alch-card">')
W('    <h2 id="alch-h" data-en="The Alchemical Great Work" data-pt="A Grande Obra Alqu\xedmica">The Alchemical Great Work</h2>')
for sym, title_en, title_pt, meaning_en, meaning_pt, use_en, use_pt in alch_blocks:
    W(f'    <div class="alch-block">')
    W(f'      <div class="alch-title"><span class="s">{sym}</span> <span data-en="{title_en}" data-pt="{title_pt}">{title_en}</span></div>')
    W(f'      <div class="alch-text"><strong class="lbl-meaning">Meaning:</strong> <span data-en="{meaning_en}" data-pt="{meaning_pt}">{meaning_en}</span></div>')
    W(f'      <div class="alch-text"><strong class="lbl-use">Symbolic Use:</strong> <span data-en="{use_en}" data-pt="{use_pt}">{use_en}</span></div>')
    W(f"    </div>")

W('    <div class="alch-block">')
W('      <div class="alch-title" id="tria-title" data-en="Tria Prima \u2014 The Three Primes" data-pt="Tria Prima \u2014 Os Tr\xeas Primeiros">Tria Prima \u2014 The Three Primes</div>')
W('      <div class="alch-text" id="tria-desc" data-en="Sulfur, Mercury, and Salt together are the three essential principles of creation and transformation:" data-pt="Enxofre, Merc\xfario e Sal s\xe3o juntos os tr\xeas princ\xedpios essenciais da cria\xe7\xe3o e transforma\xe7\xe3o:">Sulfur, Mercury, and Salt together are the three essential principles of creation and transformation:</div>')
W('      <ul style="font-size:13.5px;color:#444;line-height:1.7;">')
W('        <li id="tria-s" data-en="\U0001f70d Sulfur \u2014 the soul, the active principle" data-pt="\U0001f70d Enxofre \u2014 a alma, o princ\xedpio ativo">\U0001f70d Sulfur \u2014 the soul, the active principle</li>')
W('        <li id="tria-m" data-en="\u263f Mercury \u2014 the spirit, the volatile principle" data-pt="\u263f Merc\xfario \u2014 o esp\xedrito, o princ\xedpio vol\xe1til">\u263f Mercury \u2014 the spirit, the volatile principle</li>')
W('        <li id="tria-sa" data-en="\U0001f714 Salt \u2014 the body, the stabilizing principle" data-pt="\U0001f714 Sal \u2014 o corpo, o princ\xedpio estabilizador">\U0001f714 Salt \u2014 the body, the stabilizing principle</li>')
W("      </ul>")
W("    </div>")
W("    </div>")  # alch-card
W("  </div>")   # tab-pane
W("  </div>")   # panel-inner
W("</div>")     # panel

# --------- JS ---------
W("<script>")
W(f"const SEPH = {json.dumps(js_seph)};")
W(f"const PATHS = {json.dumps(js_paths)};")
W("""
const L = {
  en: {
    tab_seph:"Sephirot", tab_paths:"Paths & Tarot", tab_alch:"Alchemy",
    btn_show:"Show All Labels", btn_hide:"Hide All Labels", btn_clear:"Clear Selection",
    th_seph:"Sephirot", th_planet:"Planet", th_element:"Element", th_metal:"Metal",
    th_num:"#", th_letter:"Letter", th_tarot:"Tarot", th_type:"Type", th_attr:"Attribution",
    info_connects:"Connects", info_tarot:"Tarot", info_type:"Type", info_attr:"Attribution",
    info_alchem:"Alchemical", info_planet_s:"Planet / Influence", info_metal:"Alchemical Metal",
    meaning:"Meaning:", sym_use:"Symbolic Use:",
    dock_open:"\u25B6", dock_close:"\u25C0"
  },
  pt: {
    tab_seph:"Sefirot", tab_paths:"Caminhos & Tarot", tab_alch:"Alquimia",
    btn_show:"Mostrar Todos", btn_hide:"Esconder R\xf3tulos", btn_clear:"Limpar Sele\xe7\xe3o",
    th_seph:"Sefirot", th_planet:"Planeta", th_element:"Elemento", th_metal:"Metal",
    th_num:"#", th_letter:"Letra", th_tarot:"Tarot", th_type:"Tipo", th_attr:"Atribui\xe7\xe3o",
    info_connects:"Conecta", info_tarot:"Tarot", info_type:"Tipo", info_attr:"Atribui\xe7\xe3o",
    info_alchem:"Alqu\xedmico", info_planet_s:"Planeta / Influ\xeancia", info_metal:"Metal Alqu\xedmico",
    meaning:"Significado:", sym_use:"Uso Simb\xf3lico:",
    dock_open:"\u25B6", dock_close:"\u25C0"
  }
};

let lang = "en";
let sys = "gd";
let selectedPath = null;
let selectedSphere = null;
let showAll = false;
let panelOpen = true;

// --- LANGUAGE ---
function setLang(e, newLang) {
  e.stopPropagation();
  lang = newLang;
  document.getElementById("btnLangEN").classList.toggle("active", lang === "en");
  document.getElementById("btnLangPT").classList.toggle("active", lang === "pt");
  applyLang();
}

function setSys(e, newSys) {
  if (e) e.stopPropagation();
  sys = newSys;
  document.getElementById("btnSysGD").classList.toggle("active", sys === "gd");
  document.getElementById("btnSysTH").classList.toggle("active", sys === "th");
  applySystem();
}

function applySystem() {
  // Update path labels on the SVG
  for (let pid = 0; pid < 22; pid++) {
    const lnum = document.getElementById("lnum_" + pid);
    const lname = document.getElementById("lname_" + pid);
    if (!lnum || !lname) break;

    lnum.textContent = lnum.getAttribute("data-" + sys);
    
    // Based on sys and lang we choose which data attr to read
    const attrName = sys === "gd" ? "ger" : "th"; // map to data-enger, data-ptger, data-enth, data-ptth
    const comb = lang + attrName;
    lname.textContent = lname.getAttribute("data-" + comb);
    
    // update tables
    const td_tarot = document.getElementById("tbl_path_tarot_" + pid);
    if (td_tarot) {
      td_tarot.textContent = td_tarot.getAttribute("data-" + comb);
    }
  }

  applySystem();
  // refresh info panel if visible
  if (selectedPath !== null) refreshPathInfo(selectedPath);
}

// Hook applySystem inside applyLang to update textual values on language change

function applyLang() {
  const l = L[lang];
  // tabs
  document.getElementById("tb-seph").textContent = l.tab_seph;
  document.getElementById("tb-paths").textContent = l.tab_paths;
  document.getElementById("tb-alch").textContent = l.tab_alch;
  // toolbar
  const bta = document.getElementById("btnToggleAll");
  bta.textContent = showAll ? l.btn_hide : l.btn_show;
  document.getElementById("btnClear").textContent = l.btn_clear;
  // table headers
  setT("th-seph", l.th_seph); setT("th-planet", l.th_planet);
  setT("th-element", l.th_element); setT("th-metal", l.th_metal);
  setT("th-num", l.th_num); setT("th-letter", l.th_letter);
  setT("th-tarot", l.th_tarot); setT("th-type", l.th_type); setT("th-attr", l.th_attr);
  // every [data-en] element
  document.querySelectorAll("[data-en]").forEach(el => {
    el.textContent = el.getAttribute("data-" + lang);
  });
  // alchemy labels
  document.querySelectorAll(".lbl-meaning").forEach(el => el.textContent = l.meaning);
  document.querySelectorAll(".lbl-use").forEach(el => el.textContent = l.sym_use);
  // dock btn
  document.getElementById("dockBtn").innerHTML = panelOpen ? l.dock_open : l.dock_close;
  applySystem();
  // refresh info panel if visible
  if (selectedPath !== null) refreshPathInfo(selectedPath);
  if (selectedSphere !== null) refreshSphereInfo(selectedSphere);
}
function setT(id, txt) { const el = document.getElementById(id); if (el) el.textContent = txt; }

// --- LABEL STATE ---
function applyLabelState(pid, visible, scaled) {
  const el = document.getElementById("label_" + pid);
  if (!el) return;
  el.style.opacity = visible ? "1" : "0";
  el.style.transform = scaled ? "scale(1.18)" : "scale(1)";
}

function toggleAllLabels(e) {
  e.stopPropagation();
  showAll = !showAll;
  const btn = document.getElementById("btnToggleAll");
  btn.classList.toggle("active", showAll);
  btn.textContent = showAll ? L[lang].btn_hide : L[lang].btn_show;
  for (let pid = 0; pid < 22; pid++) {
    const sel = selectedPath === pid;
    applyLabelState(pid, showAll || sel, sel);
  }
}

// --- PATH SELECTION ---
function selectPath(e, pid) {
  e.stopPropagation();
  // deselect sphere
  if (selectedSphere !== null) {
    document.getElementById("seph_" + selectedSphere)?.classList.remove("selected");
    selectedSphere = null;
  }
  // deselect previous path
  if (selectedPath !== null && selectedPath !== pid) {
    document.getElementById("path_" + selectedPath)?.classList.remove("selected");
    if (!showAll) applyLabelState(selectedPath, false, false);
  }
  // toggle same path
  if (selectedPath === pid) {
    document.getElementById("path_" + pid)?.classList.remove("selected");
    if (!showAll) applyLabelState(pid, false, false);
    selectedPath = null;
    hideInfo();
    return;
  }
  selectedPath = pid;
  document.getElementById("path_" + pid)?.classList.add("selected");
  applyLabelState(pid, true, true);
  refreshPathInfo(pid);
}

function refreshPathInfo(pid) {
  const d = PATHS[pid];
  const l = L[lang];
  const tname = typeof d.tarot_name === "object" ? d.tarot_name[lang] : d.tarot_name;
  showInfo("#e74c3c", "Path " + d.id + ": " + d.letter + " \u2013 " + d.heb, [
    [l.info_connects, d.s1 + " \u2194 " + d.s2],
    [l.info_tarot, d.tarot + " | " + tname],
    [l.info_planet, d.planet],
    [l.info_zodiac, d.zodiac],
    [l.info_alchem, d.alchem],
  ]);
}

// --- SPHERE SELECTION ---
function selectSphere(e, key) {
  e.stopPropagation();
  if (selectedPath !== null) {
    document.getElementById("path_" + selectedPath)?.classList.remove("selected");
    if (!showAll) applyLabelState(selectedPath, false, false);
    selectedPath = null;
  }
  if (selectedSphere !== null && selectedSphere !== key) {
    document.getElementById("seph_" + selectedSphere)?.classList.remove("selected");
  }
  if (selectedSphere === key) {
    document.getElementById("seph_" + key)?.classList.remove("selected");
    selectedSphere = null;
    hideInfo();
    return;
  }
  selectedSphere = key;
  document.getElementById("seph_" + key)?.classList.add("selected");
  refreshSphereInfo(key);
}

function refreshSphereInfo(key) {
  const d = SEPH[key];
  const l = L[lang];
  if (!d) return;
  const name   = typeof d.name    === "object" ? d.name[lang]    : d.name;
  const planet = typeof d.planet  === "object" ? d.planet[lang]  : d.planet;
  const element= typeof d.element === "object" ? d.element[lang] : d.element;
  const metal  = typeof d.metal   === "object" ? d.metal[lang]   : d.metal;
  showInfo("#3498db", name, [
    [l.info_planet_s, planet],
    [l.th_element, element],
    [l.info_metal, metal],
  ]);
}

// --- INFO PANEL ---
function showInfo(color, title, rows) {
  const p = document.getElementById("infoPanel");
  p.style.borderLeftColor = color;
  let html = "<h3>" + title + "</h3>";
  for (const [label, val] of rows)
    html += '<div class="info-row"><span class="info-label">' + label + '</span><span class="sym">' + val + "</span></div>";
  p.innerHTML = html;
  p.style.display = "block";
}
function hideInfo() {
  document.getElementById("infoPanel").style.display = "none";
}

// --- BACKGROUND CLICK (clear selection) ---
function handleBgClick(e) {
  if (e.target === document.getElementById("treeWrap") || e.target === document.getElementById("treeSvg") || e.target.tagName === "svg") {
    clearSelection(e);
  }
}

function clearSelection(e) {
  if (e) e.stopPropagation();
  if (selectedPath !== null) {
    document.getElementById("path_" + selectedPath)?.classList.remove("selected");
    if (!showAll) applyLabelState(selectedPath, false, false);
    selectedPath = null;
  }
  if (selectedSphere !== null) {
    document.getElementById("seph_" + selectedSphere)?.classList.remove("selected");
    selectedSphere = null;
  }
  hideInfo();
}

// --- PANEL TOGGLE ---
function togglePanel(e) {
  if (e) e.stopPropagation();
  panelOpen = !panelOpen;
  document.getElementById("sidePanel").classList.toggle("closed", !panelOpen);
  document.getElementById("dockBtn").innerHTML = panelOpen ? L[lang].dock_open : L[lang].dock_close;
}

// --- TABS ---
function openTab(id, btn) {
  document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));
  document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
  document.getElementById(id).classList.add("active");
  btn.classList.add("active");
}
""")
W("</script>")
W("</body>")
W("</html>")

with open("d:/TreeOfLife/TreeOfLife.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines))

print("Done!")
