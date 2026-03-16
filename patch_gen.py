import re

with open("d:/TreeOfLife/gen.py", "r", encoding="utf-8") as f:
    src = f.read()

# 1. Update L dict
en_update1 = '"btn_clear": "Clear Selection",\n        "btn_sys_gd": "Golden Dawn",\n        "btn_sys_th": "Thelema",\n'
src = src.replace('"btn_clear": "Clear Selection",', en_update1)

en_update2 = '"th_planet": "Planet",\n        "th_type": "Type",\n        "th_attr": "Attribution",\n'
src = src.replace('"th_planet": "Planet",', en_update2)

en_update3 = '"info_planet": "Planetary",\n        "info_type": "Type",\n        "info_attr": "Attribution",\n'
src = src.replace('"info_planet": "Planetary",', en_update3)


pt_update1 = '"btn_clear": "Limpar Sele\\xe7\\xe3o",\n        "btn_sys_gd": "Golden Dawn",\n        "btn_sys_th": "Thelema",\n'
src = src.replace('"btn_clear": "Limpar Sele\\xe7\\xe3o",', pt_update1)

pt_update2 = '"th_planet": "Planeta",\n        "th_type": "Tipo",\n        "th_attr": "Atribui\\xe7\\xe3o",\n'
src = src.replace('"th_planet": "Planeta",', pt_update2)

pt_update3 = '"info_planet": "Planet\\xe1rio",\n        "info_type": "Tipo",\n        "info_attr": "Atribui\\xe7\\xe3o",\n'
src = src.replace('"info_planet": "Planet\\xe1rio",', pt_update3)

# 2. Update spheres Chokmah and Malkuth symbols
src = src.replace('"#1e90ff", "\\u2609",     {"en": "Chockmah",  "pt": "Chockmah"}),', '"#1e90ff", "\\u2605",     {"en": "Chokmah",  "pt": "Chokmah"}),')
src = src.replace('"#daa520", "\\u2644",     {"en": "Malkuth",   "pt": "Malkuth"}),', '"#daa520", "\\u2641",     {"en": "Malkuth",   "pt": "Malkuth"}),') # 🜃 isn't widely supported in standard fonts as circle, maybe ♁ (Earth \u2641)

# 3. Replace paths array entirely
old_paths_block = re.search(r'paths = \[\n.*?\]\n', src, re.DOTALL).group(0)

new_paths_block = """paths = [
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
"""
src = src.replace(old_paths_block, new_paths_block)


# 4. Replace sefirot_data array
old_sefirot_block = re.search(r'sefirot_data = \[\n.*?\]\n', src, re.DOTALL).group(0)

new_sefirot_block = """sefirot_data = [
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
"""
src = src.replace(old_sefirot_block, new_sefirot_block)

# 5. Fix JS paths iteration
old_js_paths_iter = re.search(r'js_paths = \{\}\nfor pid, .*? in paths:.*?\}', src, re.DOTALL).group(0)
new_js_paths_iter = """js_paths = {}
for pid, letter, heb, s1, s2, tarot_gd_num, tarot_gd_bi, tarot_th_num, tarot_th_bi, t, nx, ny, dist, attr_type_bi, attr_val_bi in paths:
    js_paths[str(pid)] = {
        "id": pid, "letter": letter, "heb": heb,
        "s1": s1, "s2": s2,
        "tarot_gd_num": tarot_gd_num, "tarot_gd_name": tarot_gd_bi,
        "tarot_th_num": tarot_th_num, "tarot_th_name": tarot_th_bi,
        "attr_type": attr_type_bi, "attr_val": attr_val_bi
    }"""
src = src.replace(old_js_paths_iter, new_js_paths_iter)

# 6. SVG generation loop for Paths
old_svg_paths = """for pid, letter, heb, s1, s2, tarot_num, tarot_bi, t, nx, ny, dist, planet, zodiac, alchem in paths:
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

    en_name = tarot_bi["en"] if isinstance(tarot_bi, dict) else tarot_bi
    pt_name = tarot_bi["pt"] if isinstance(tarot_bi, dict) else tarot_bi

    W(f'    <g id="path_{pid}" class="path-g" onclick="selectPath(event,{pid})">')
    W(f'      <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="transparent" stroke-width="22" />')
    W(f'      <line class="vis-line" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#666" stroke-width="3" />')
    W(f'    </g>')

    # Label: 3 lines: "Aleph – א" / "III" / "The Empress"
    W(f'    <g id="label_{pid}" class="path-label" style="opacity:0;pointer-events:none;transform-origin:{lx}px {ly}px;transform:scale(0.85);">')
    W(f'      <line x1="{mx}" y1="{my}" x2="{lx}" y2="{ly}" stroke="#bbb" stroke-width="1.5" stroke-dasharray="4,3" />')
    W(f'      <rect x="{lx-bw/2}" y="{ly-bh/2}" width="{bw}" height="{bh}" rx="10" fill="#fff" stroke="#555" stroke-width="1.5" />')
    W(f'      <text x="{lx}" y="{ly-15}" text-anchor="middle" dominant-baseline="middle" font-weight="bold" font-size="13" fill="#222">{letter} \u2013 {heb}</text>')
    W(f'      <text x="{lx}" y="{ly}" text-anchor="middle" dominant-baseline="middle" font-size="12" fill="#777">{tarot_num}</text>')
    W(f'      <text id="lname_{pid}" x="{lx}" y="{ly+14}" text-anchor="middle" dominant-baseline="middle" font-size="12" fill="#444" data-en="{en_name}" data-pt="{pt_name}">{en_name}</text>')
    W(f'    </g>')"""

new_svg_paths = """for pid, letter, heb, s1, s2, tarot_gd_num, tarot_gd_bi, tarot_th_num, tarot_th_bi, t, nx, ny, dist, attr_type_bi, attr_val_bi in paths:
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
    W(f'    </g>')"""
src = src.replace(old_svg_paths, new_svg_paths)

# 7. Add .sys-toggle to CSS
css_search = r'/\* LANG TOGGLE \*/.*?\.lang-toggle button\.active \{.*?\}\n'
css_replacement = """/* LANG/SYS TOGGLES */
    .lang-toggle, .sys-toggle { display: flex; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,.15); }
    .lang-toggle button, .sys-toggle button { margin: 0; border-radius: 0; box-shadow: none; background: #34495e; color: #95a5a6; flex: 1; padding: 8px 10px; border-bottom: 3px solid transparent; }
    .lang-toggle button:hover, .sys-toggle button:hover { background: #2c3e50; color: #fff; }
    .lang-toggle button.active, .sys-toggle button.active { background: #2c3e50; color: #1abc9c; border-bottom-color: #1abc9c; }
"""
src = re.sub(css_search, css_replacement, src, flags=re.DOTALL)

# 8. Add HTML for System Toggle
toolbar_search = r'<div class="lang-toggle">.*?</div>'
toolbar_replacement = """<div class="lang-toggle">
      <button id="btnLangEN" class="active" onclick="setLang(event, 'en')">EN-US</button>
      <button id="btnLangPT" onclick="setLang(event, 'pt')">PT-BR</button>
    </div>
    <div class="sys-toggle">
      <button id="btnSysGD" class="active" onclick="setSys(event, 'gd')" data-en="Golden Dawn" data-pt="Golden Dawn">Golden Dawn</button>
      <button id="btnSysTH" onclick="setSys(event, 'th')" data-en="Thelema" data-pt="Thelema">Thelema</button>
    </div>"""
src = re.sub(toolbar_search, toolbar_replacement, src, flags=re.DOTALL)

# 9. Update HTML paths table generated 
old_html_paths_table_th = """W('        <th id="th-planet2">Planet</th>')
W('        <th id="th-zodiac">Zodiac</th>')"""
new_html_paths_table_th = """W('        <th id="th-type">Type</th>')
W('        <th id="th-attr">Attribution</th>')"""
src = src.replace(old_html_paths_table_th, new_html_paths_table_th)

old_html_paths_iter = """for pid, letter, heb, s1, s2, tarot_num, tarot_bi, t, nx, ny, dist, planet, zodiac, alchem in paths:
    en_tn = tarot_bi["en"] if isinstance(tarot_bi, dict) else tarot_bi
    pt_tn = tarot_bi["pt"] if isinstance(tarot_bi, dict) else tarot_bi
    planet_val = planet["en"] if isinstance(planet, dict) else planet
    W(f'      <tr onclick="selectPath(event,{pid})">')
    W(f'        <td class="c-grey">{pid}</td>')
    W(f'        <td class="c-red">{letter} \u2013 {heb}</td>')
    W(f'        <td class="c-teal" data-en="{tarot_num} | {en_tn}" data-pt="{tarot_num} | {pt_tn}">{tarot_num} | {en_tn}</td>')
    W(f'        <td class="sym">{planet_val}</td>')
    W(f'        <td>{zodiac}</td>')
    W("      </tr>")"""

new_html_paths_iter = """for pid, letter, heb, s1, s2, tarot_gd_num, tarot_gd_bi, tarot_th_num, tarot_th_bi, t, nx, ny, dist, attr_type_bi, attr_val_bi in paths:
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
    W("      </tr>")"""
src = src.replace(old_html_paths_iter, new_html_paths_iter)


# 10. Update translations dictionary in JS string
js_l_repl = """    th_seph:"Sephirot", th_planet:"Planet", th_element:"Element", th_metal:"Metal",
    th_num:"#", th_letter:"Letter", th_tarot:"Tarot", th_planet2:"Planet", th_zodiac:"Zodiac",
    info_connects:"Connects", info_tarot:"Tarot", info_planet:"Planetary", info_zodiac:"Zodiac",
    info_alchem:"Alchemical", info_planet_s:"Planet / Influence", info_metal:"Alchemical Metal",
"""
js_l_repl_en_new = """    th_seph:"Sephirot", th_planet:"Planet", th_element:"Element", th_metal:"Metal",
    th_num:"#", th_letter:"Letter", th_tarot:"Tarot", th_type:"Type", th_attr:"Attribution",
    info_connects:"Connects", info_tarot:"Tarot", info_type:"Type", info_attr:"Attribution",
    info_alchem:"Alchemical", info_planet_s:"Planet / Influence", info_metal:"Alchemical Metal",
"""
src = src.replace(js_l_repl, js_l_repl_en_new)

js_l_repl_pt = """    th_seph:"Sefirot", th_planet:"Planeta", th_element:"Elemento", th_metal:"Metal",
    th_num:"#", th_letter:"Letra", th_tarot:"Tarot", th_planet2:"Planeta", th_zodiac:"Zo\\xedaco",
    info_connects:"Conecta", info_tarot:"Tarot", info_planet:"Planet\\xe1rio", info_zodiac:"Zo\\xedaco",
    info_alchem:"Alqu\\xedmico", info_planet_s:"Planeta / Influ\\xeancia", info_metal:"Metal Alqu\\xedmico",
"""
js_l_repl_pt_new = """    th_seph:"Sefirot", th_planet:"Planeta", th_element:"Elemento", th_metal:"Metal",
    th_num:"#", th_letter:"Letra", th_tarot:"Tarot", th_type:"Tipo", th_attr:"Atribui\\xe7\\xe3o",
    info_connects:"Conecta", info_tarot:"Tarot", info_type:"Tipo", info_attr:"Atribui\\xe7\\xe3o",
    info_alchem:"Alqu\\xedmico", info_planet_s:"Planeta / Influ\\xeancia", info_metal:"Metal Alqu\\xedmico",
"""
src = src.replace(js_l_repl_pt, js_l_repl_pt_new)


# 11. Update JS logic
src = src.replace('let lang = "en";', 'let lang = "en";\nlet sys = "gd";')

apply_lang_old = """  setT("th-num", l.th_num); setT("th-letter", l.th_letter);
  setT("th-tarot", l.th_tarot); setT("th-planet2", l.th_planet2); setT("th-zodiac", l.th_zodiac);"""
apply_lang_new = """  setT("th-num", l.th_num); setT("th-letter", l.th_letter);
  setT("th-tarot", l.th_tarot); setT("th-type", l.th_type); setT("th-attr", l.th_attr);"""
src = src.replace(apply_lang_old, apply_lang_new)

# Add setSys logic
sys_toggle_js_injection = """function setSys(e, newSys) {
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

  // refresh info panel if visible
  if (selectedPath !== null) refreshPathInfo(selectedPath);
}

// Hook applySystem inside applyLang to update textual values on language change
"""
src = src.replace('function applyLang() {', sys_toggle_js_injection + '\nfunction applyLang() {')
src = src.replace('// refresh info panel if visible', 'applySystem();\n  // refresh info panel if visible')

# Fix refreshPathInfo implementation
old_refresh = """function refreshPathInfo(pid) {
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
}"""

new_refresh = """function refreshPathInfo(pid) {
  const d = PATHS[pid];
  const l = L[lang];
  const tname = sys === 'gd' ? d.tarot_gd_name[lang] : d.tarot_th_name[lang];
  const tnum = sys === 'gd' ? d.tarot_gd_num : d.tarot_th_num;
  const attr_type = d.attr_type[lang];
  const attr_val = d.attr_val[lang];
  
  showInfo("#e74c3c", "Path " + d.id + ": " + d.letter + " \u2013 " + d.heb, [
    [l.info_connects, d.s1 + " \u2194 " + d.s2],
    [l.info_tarot, tnum + " | " + tname],
    [l.info_type, attr_type],
    [l.info_attr, attr_val],
  ]);
}"""
src = src.replace(old_refresh, new_refresh)


with open("d:/TreeOfLife/gen.py", "w", encoding="utf-8") as f:
    f.write(src)
print("done rewriting gen.py")
