#!/usr/bin/env python3
"""Builds the Bait Sitty static site into this folder."""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))

BASE = "https://baitsittyrestaurant.com/wp-content/uploads/"
LOGO = BASE + "2025/10/WhatsApp-Image-2025-10-30-at-9.16.00-AM-Edited-e1761835567269.png"
IMG_ABOUT = BASE + "2025/11/WhatsApp-Image-2025-11-04-at-3.01.04-PM.jpeg"
IMG_AMBIENCE = BASE + "2025/11/WhatsApp-Image-2025-11-04-at-3.22.38-PM-1.jpeg"
IMG_MENU = BASE + "2025/11/WhatsApp-Image-2025-11-01-at-10.30.06-AM-3-e1762294048363.jpeg"
GALLERY = [
    "2025/11/WhatsApp-Image-2025-11-02-at-2.49.19-AM.jpeg",
    "2025/11/WhatsApp-Image-2025-11-02-at-2.39.12-AM.jpeg",
    "2025/11/WhatsApp-Image-2025-11-01-at-12.04.28-PM.jpeg",
    "2025/11/WhatsApp-Image-2025-11-01-at-10.30.06-AM.jpeg",
    "2025/11/WhatsApp-Image-2025-11-01-at-10.30.06-AM-1.jpeg",
    "2025/11/WhatsApp-Image-2025-11-01-at-10.30.06-AM-3-e1762294048363.jpeg",
    "2025/11/WhatsApp-Image-2025-11-01-at-11.02.34-AM-1.jpeg",
    "2025/11/WhatsApp-Image-2025-11-01-at-10.19.37-AM.jpeg",
    "2025/11/WhatsApp-Image-2025-11-02-at-2.49.20-AM.jpeg",
    "2025/11/WhatsApp-Image-2025-11-04-at-3.01.04-PM-3.jpeg",
    "2025/11/WhatsApp-Image-2025-11-04-at-3.01.04-PM-2.jpeg",
    "2025/11/WhatsApp-Image-2025-11-04-at-3.01.04-PM-1.jpeg",
    "2025/11/WhatsApp-Image-2025-11-04-at-3.01.04-PM.jpeg",
    "2025/11/WhatsApp-Image-2025-11-05-at-00.32.41_8d3b6da3.jpg",
    "2025/11/WhatsApp-Image-2025-11-02-at-2.44.23-AM.jpeg",
]

INSTAGRAM = "https://www.instagram.com/baitsittyrestaurant?igsh=MTJwc3AwNGZvd3J4ag=="
TIKTOK = "https://www.tiktok.com/@baitsitty?_r=1&_t=ZS-912yYYXIp20"
EMAIL = "info@baitsittyrestaurant.com"
PHONE_DISPLAY = "647.400.0488"
PHONE_TEL = "+16474000488"
ADDRESS_1 = "3145 Dundas St W, Unit #1"
ADDRESS_2 = "Mississauga, ON L5L 5V8"
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=3145+Dundas+St+W+Mississauga+ON"
MAPS_EMBED = "https://maps.google.com/maps?q=3145%20Dundas%20St%20W%20Mississauga&t=m&z=14&output=embed&iwloc=near"

HOURS = [
    ("Saturday", "10 AM to 1 AM"),
    ("Sunday", "10 AM to 11 PM"),
    ("Monday", "5 PM to 11 PM"),
    ("Tuesday", "11 AM to 11 PM"),
    ("Wednesday", "11 AM to 11 PM"),
    ("Thursday", "11 AM to midnight"),
    ("Friday", "11 AM to 1 AM"),
]

NAV = [
    ("home", "index.html", "Home"),
    ("about", "about.html", "About"),
    ("menu", "menu.html", "Menu"),
    ("gallery", "gallery.html", "Gallery"),
    ("catering", "catering.html", "Catering and events"),
    ("contact", "contact.html", "Contact"),
]

# ---------------------------------------------------------------- assets

def tatreez_svg(color, bg=None):
    motif = [
        "....X....",
        "...XXX...",
        "..XX.XX..",
        ".XX.X.XX.",
        "XX.XXX.XX",
        ".XX.X.XX.",
        "..XX.XX..",
        "...XXX...",
        "....X....",
    ]
    s = 3
    pad = 1
    tile = (9 + 2 * pad) * s
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{tile}" height="{tile}" viewBox="0 0 {tile} {tile}">']
    if bg:
        parts.append(f'<rect width="{tile}" height="{tile}" fill="{bg}"/>')
    parts.append(f'<g stroke="{color}" stroke-width="0.85" stroke-linecap="square" fill="none">')
    for r, row in enumerate(motif):
        for c, ch in enumerate(row):
            if ch == "X":
                x = (c + pad) * s
                y = (r + pad) * s
                parts.append(f'<path d="M{x+.3} {y+.3}L{x+s-.3} {y+s-.3}M{x+s-.3} {y+.3}L{x+.3} {y+s-.3}"/>')
    parts.append("</g></svg>")
    return "".join(parts)


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


write("assets/tatreez-red.svg", tatreez_svg("#7b1426"))
write("assets/tatreez-brass.svg", tatreez_svg("#d9b45a"))
write(
    "assets/favicon.svg",
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#7b1426"/>'
    '<path d="M32 10 L48 32 L32 54 L16 32 Z" fill="none" stroke="#d9b45a" stroke-width="4"/>'
    '<path d="M32 22 L40 32 L32 42 L24 32 Z" fill="#d9b45a"/></svg>',
)

# ---------------------------------------------------------------- menu data

def P(v):
    return "$" + v

MENU = [
    {
        "id": "brunch", "label": "Brunch",
        "intro": "Bait Sitty’s brunch, built around freshly baked manakeesh and the dishes Sitty put on the table at breakfast.",
        "groups": [
            {"title": "Freshly baked manakeesh", "items": [
                ("Cheese Manakeesh", P("8"), "Topped with nabulsi cheese.", None),
                ("Lahmeh Manakeesh", P("8"), "Topped with ground beef and pomegranate molasses.", None),
                ("Cheese and Zaatar Manakeesh", P("8"), "Topped with jibneh, nabulsi and Palestinian zaatar spread.", None),
                ("Egg and Cheese Manakeesh", P("10"), "Topped with jibneh, nabulsi and fresh eggs.", None),
                ("Soujok and Cheese Manakeesh", P("10"), "Topped with jibneh, nabulsi and fresh aged sausage.", None),
                ("Zaatar Manakeesh", P("7"), "Topped with Palestinian zaatar spread.", None),
                ("Labneh Manakeesh", P("7"), "Topped with labneh and mint.", None),
                ("Egg Manakeesh", P("8"), "Topped with fresh eggs.", None),
                ("Muhammarah Manakeesh", P("10"), "Topped with roasted red peppers, pomegranate molasses and walnuts.", None),
                ("Sabanekh Manakeesh", P("9"), "Topped with fresh sabanekh (spinach), onions and sumac.", None),
            ]},
            {"title": "Sitty’s sides", "items": [
                ("Zait and Zaatar", P("5"), "A classic Middle Eastern dip of olive oil and zaatar spice blend.", None),
                ("Pickles and Olives", P("7"), "Assorted pickles, turnips, radish, cucumber, mint and olives.", None),
                ("Ka’ek Al Quds", P("3"), "Freshly baked, golden crust, soft inside, topped generously with toasted sesame seeds.", "Jerusalem sesame bread"),
            ]},
            {"title": "Sitty’s favourites", "items": [
                ("Ftoor Sitty", P("48"), "Qoudsiyeh, foul, falafel, labneh zrar, zait and zaatar, pickles and olives.", "Grandma’s breakfast"),
                ("Kebdeh", P("17"), "Pan seared chicken liver, caramelized onions and garlic. Drizzled with pomegranate molasses.", None),
                ("Falafel", P("9"), "Chickpeas, parsley and onions. Served with tahini sauce.", None),
                ("Sitty’s Foul", P("9"), "Cooked fava beans, olive oil, tomato, lemon juice, chickpeas and daqa (dressing).", None),
                ("Hummus Be Lahmeh", P("17"), "Hummus topped with beef tenderloin.", None),
                ("Hummus", P("11"), "Chickpea puree, lemon and tahini.", None),
                ("Kafta Arayes", P("17"), "Traditional pita bread stuffed with kafta. Served with a side of tahini salad.", None),
            ]},
            {"title": "Fresh off the claypot", "items": [
                ("Fattet Hummus", P("16"), "Chickpea puree, tahini, yogurt, dried chickpeas, fried pita, daqa (dressing) and slivered almonds. Add meat for $5.", None),
                ("Jibneh Nabulsi", P("18"), "Seared nabulsi cheese, cherry tomato, fresh slivered garlic, basil and mint. Drizzled with olive oil and lemon juice.", None),
                ("Shakshooka", P("15"), "Tomato sauce and onions. Topped with sunny side up eggs.", None),
                ("Soujok and Egg", P("17"), "Aged beef sausage, tomatoes and onions. Tossed in lemon, topped with sunny side up eggs.", None),
            ]},
        ],
    },
    {
        "id": "starters", "label": "Starters",
        "intro": None,
        "groups": [
            {"title": None, "items": [
                ("Soup of the day", P("6"), "Kindly ask your server.", None),
                ("Zait and Zaatar", P("5"), "Thyme (zaatar) and olive oil.", None),
                ("Jibneh Nabulsi", P("18"), "Grilled nabulsi cheese, cherry tomato, fresh sliced garlic, basil and mint. Drizzled with olive oil and lemon juice.", None),
                ("Kafta Arayes", P("19"), "Traditional pita bread stuffed with kafta, and tahiniyeh salad.", None),
                ("Pickles and Olives", P("7"), "Assorted pickles, turnips, radish, cucumber, mint and olives.", None),
                ("Warak Enab", P("13"), "Grape leaves stuffed with rice, tomato, onion, parsley, mint and pomegranate molasses.", None),
                ("Saltet Al Raheb", P("13"), "Roasted eggplant, capsicum, scallions, parsley, cilantro, garlic and lemon juice. Drizzled with pomegranate molasses.", None),
            ]},
        ],
    },
    {
        "id": "dips", "label": "Dips",
        "intro": None,
        "groups": [
            {"title": None, "items": [
                ("Hummus Be Lahmeh", P("17"), "Hummus topped with beef tenderloin and sliced almonds.", None),
                ("Hummus", P("11"), "Chickpea puree, lemon and tahini.", None),
                ("Labneh Zrar", P("12"), "In house hand pressed yogurt balls (labneh), mint, sumac and thyme (zaatar).", None),
                ("Muhammarah", P("12"), "Roasted red pepper, walnuts and pomegranate.", None),
                ("Mutabal", P("11"), "Roasted eggplant puree, tahini and lemon.", None),
                ("Sampler", P("25"), "Your choice of three dips served with bread.", None),
                ("Hakooret Sitty", P("58"), "Hummus, mutabal, muhammarah, labneh harah, saltet tahiniyeh, saltet al raheb, saltet falaha and batenjan sitty.", None),
            ]},
        ],
    },
    {
        "id": "hot-meze", "label": "Hot meze",
        "intro": None,
        "groups": [
            {"title": None, "items": [
                ("Falafel", P("9"), "Ground chickpeas with parsley and onions.", None),
                ("Soujok", P("16"), "In house aged beef sausage served with tomatoes and onions, tossed in lemon.", None),
                ("Fresh Cut Fries", P("8"), "Fresh cut fries seasoned in house.", None),
                ("Batata Harah", P("9"), "Fried potatoes, cilantro, spicy (shatta) sauce and garlic sauce.", None),
                ("Kebbe", P("16"), "Cracked wheat stuffed with ground beef, onions and sliced almonds.", None),
                ("Kebdeh", P("17"), "Pan seared chicken liver, served with caramelized onions and garlic, drizzled in pomegranate molasses.", None),
                ("Halfmoon Cheese Bites", P("13"), "Moon shaped mixed four cheese bites.", None),
                ("Zahra Be Tahini", P("12"), "Baked cauliflower, served with tahini sauce and caramelized onions.", None),
            ]},
        ],
    },
    {
        "id": "salads", "label": "Salads",
        "intro": None,
        "groups": [
            {"title": None, "items": [
                ("Tabouleh", P("19"), "Parsley, tomatoes, green onions, bulgur, lemon and olive oil.", None),
                ("Fatoush", P("19"), "Tomatoes, cucumber, red onions, radish, lettuce and bell peppers, topped with fried pieces of pita bread.", None),
                ("Sitty’s Salad", P("20"), "Fried eggplant, potatoes, chickpeas, corn, lettuce, onions, fried pita and Sitty’s dressing.", None),
                ("Jarjeer Salad", P("18"), "Arugula, red onions, cherry tomatoes, walnuts, mushrooms, balsamic vinegar, olive oil, sumac and mint.", None),
                ("Falafel Salad", P("19"), "Falafel with tomatoes, cucumber, red onions, radish, lettuce and turnip, topped with tahini.", None),
            ]},
        ],
    },
    {
        "id": "signature", "label": "Sitty’s signature",
        "intro": None,
        "groups": [
            {"title": None, "items": [
                ("Levantine Bass", P("40"), "Fresh sea bass roasted in the oven. Served with tahini salad and spicy potatoes with tomato sauce.", None),
                ("Sayadiyet Sitty", P("35"), "Fresh sea bass fillet. Served with rice and herbs, caramelized onions and sliced almonds with tomato sauce.", None),
                ("Dajaj Sitty", P("27"), "Fire roasted supreme chicken, taboon bread, sumac, onions and yogurt. Available in breast or leg.", "Musakhan"),
                ("Farooj Mashwe", "$41 whole, $30 half", "Whole boneless chicken, spicy potatoes, pickles, olives and garlic sauce. Available whole or half.", None),
                ("In House Special", None, "Kindly ask your server.", None),
            ]},
        ],
    },
    {
        "id": "claypot", "label": "Claypot signatures",
        "intro": "Served with your choice of rice or bulgur.",
        "groups": [
            {"title": None, "items": [
                ("Kafta Be Tahini", P("29"), "Minced lamb and beef cooked in a claypot. Potatoes in tahini sauce topped with caramelized onions.", None),
                ("Fattet Kabob", P("30"), "Kafta kabob cooked in a claypot with eggplant, tomato sauce and garlic. Topped with fried pieces of pita bread, yogurt, mint sauce, pomegranate seeds and sliced almonds.", None),
                ("Costoletta", P("38"), "Classic Ontario lamb chops with rosemary. Potatoes drizzled in Sitty sauce. Baked in a claypot.", "Lamb chops"),
                ("Sitty O Kanayinyah", P("26"), "Kebbe and beef dumplings in yogurt mint sauce and garlic.", None),
                ("Mjadara", P("21"), "A mixed plate of bulgur, brown lentils and mixed bell pepper. Topped with caramelized onions, with falaha salad.", None),
            ]},
        ],
    },
    {
        "id": "grill", "label": "Hash and Nash BBQ",
        "intro": "Served with fatoush, batata harah, rice, and garlic sauce or tahini sauce.",
        "groups": [
            {"title": None, "items": [
                ("Shish Taouk", P("28"), "Chicken breast cubes.", None),
                ("Kafta Kabob", P("28"), "In house minced ground lamb and beef mix.", None),
                ("Filet Mignon", P("33"), "Beef tenderloin cubes.", None),
                ("Mix Mashawi", P("36"), "Shish taouk, filet mignon and kafta kabob.", None),
                ("Mix Mashawi for 2", P("75"), "Shish taouk, filet mignon and kafta kabob (two of each).", None),
                ("Family Mix Mashawi", P("142"), "Shish taouk, filet mignon and kafta kabob (four of each). Covered with a layer of baked dough.", None),
                ("Sitty’s Mix Mashawi", P("240"), "Shish taouk, filet mignon, kafta kabob and lamb chops (four of each). Served with hummus and mutabal or muhammarah. Covered with a layer of baked dough.", None),
            ]},
        ],
    },
    {
        "id": "sandwiches", "label": "Sandwiches",
        "intro": None,
        "groups": [
            {"title": None, "items": [
                ("Shish Taouk Sandwich", P("17"), "Grilled, with lettuce, pickles, tomatoes and garlic sauce.", None),
                ("Filet Mignon Sandwich", P("18"), "Served with tomatoes, onions, pickles, sumac and tahini sauce.", None),
                ("Kafta Kabob Sandwich", P("17"), "Served with lettuce, pickles, tomatoes and garlic sauce.", None),
                ("Vegetarian Sandwich", P("15"), "Fried cauliflower or fried potatoes, tomatoes, onions and pickles.", None),
                ("Falafel Sandwich", P("14"), "Ground chickpea served with tomatoes, onions, red cabbage and tahini.", None),
            ]},
        ],
    },
    {
        "id": "desserts", "label": "Desserts",
        "intro": None,
        "groups": [
            {"title": None, "items": [
                ("Kunafeh Nabulsi", P("9"), "A sweet and creamy dessert inspired by the famous knafeh of Nablus. Rich, cheesy and finished with a hint of syrup. Crunchy or soft available.", None),
                ("Waffle", P("11"), "Warm waffle topped with your choice of Nutella or Dubai pistachio chocolate. Dubai pistachio chocolate is an extra $3.", None),
                ("Eshta", P("8"), "Ashta (clotted cream) served with honey and pistachio. Add fruits for $3.", None),
                ("Layali Lebnan", P("8"), "Semolina pudding layered with ashta. Crushed pistachios and sweet syrup.", None),
                ("Dubai Chocolate Cup", P("16"), "Fresh strawberries layered with a pistachio cream and ashta, topped with melted chocolate.", None),
            ]},
        ],
    },
]

DRINKS = [
    ("Refreshments", [("Soft Drinks (Can)", "4"), ("Passion Fruit Soda", "6"), ("Strawberry Soda", "6"), ("Raspberry Soda", "6"), ("Sparkling Mojito (Virgin)", "6"), ("Sparkling Water", "5"), ("Bottled Water", "3"), ("Ayran", "5")]),
    ("Aseer Sitty", [("Lemon and Mint", "11"), ("Orange", "10"), ("Kiwi", "11"), ("Lemonade", "10"), ("Mango", "11"), ("Pomegranate", "11"), ("Pineapple", "10"), ("Strawberry", "10")]),
    ("Espressos", [("Vanilla Latte", "6"), ("Caramel Latte", "6"), ("Spanish Latte", "7"), ("Americano", "6"), ("Pistachio Latte", "8"), ("Hazelnut Latte", "6"), ("Matcha Latte", "9"), ("Cappuccino", "6"), ("Turkish Coffee", "4")]),
    ("Iced coffees", [("Iced Latte", "8"), ("Iced Mocha", "8"), ("Iced Vanilla Latte", "8"), ("Iced Caramel Latte", "8"), ("Iced White Mocha", "8"), ("Iced Hazelnut Latte", "9"), ("Iced Pistachio Latte", "10")]),
    ("Signatures", [("Shoroq Yaffa", "13"), ("Ramallah Refresh", "12"), ("Noor Al Quds", "15"), ("Ghorob Ramallah", "12"), ("Shams Falasteen", "13")]),
    ("Fresh smoothies", [("Lemon Mint", "11"), ("Mango", "11"), ("Berry Blend", "11"), ("Pineapple", "11"), ("Lemonade", "11"), ("Fakhfakhina", "13"), ("Strawberry", "11")]),
    ("Milkshakes", [("Avocado Eshta", "15"), ("Baskoot Shake", "12"), ("Samra Shake", "13"), ("Ward w Mawz", "12")]),
    ("Sedo’s chai", [("Mint Tea", "4"), ("Chai Al Seha (Healing)", "9"), ("Karak Chai", "5"), ("Green Tea", "4"), ("Iraqi Style Chai", "4"), ("Moroccan Style Chai", "4")]),
    ("Seasonal favourites", [("Iced Golden Chai", "12"), ("Layali Matcha", "13"), ("Midday Tiramisu", "12"), ("Ward Matcha Latte", "12")]),
]

# ---------------------------------------------------------------- templates

def e(s):
    return html.escape(s, quote=True)


def hours_rows(cls=""):
    return "".join(
        f'<tr data-day="{d}"><th scope="row">{d}</th><td>{t}</td></tr>' for d, t in HOURS
    )


def render_item(name, price, desc, gloss):
    head = f'<h4>{e(name)}</h4>'
    if price:
        head += f'<span class="dots" aria-hidden="true"></span><span class="price">{e(price)}</span>'
    g = f'<p class="gloss">{e(gloss)}</p>' if gloss else ""
    d = f'<p class="desc">{e(desc)}</p>' if desc else ""
    return f'<li class="item"><div class="item-head">{head}</div>{g}{d}</li>'


def render_menu_body():
    out = []
    for cat in MENU:
        out.append(f'<section class="cat" id="{cat["id"]}" data-cat="{e(cat["label"])}">')
        out.append(f'<h2>{e(cat["label"])}</h2>')
        if cat["intro"]:
            out.append(f'<p class="cat-intro">{e(cat["intro"])}</p>')
        for g in cat["groups"]:
            out.append('<div class="group">')
            if g["title"]:
                out.append(f'<h3>{e(g["title"])}</h3>')
            out.append('<ul class="items">' + "".join(render_item(*it) for it in g["items"]) + "</ul>")
            out.append("</div>")
        out.append("</section>")
    # drinks
    out.append('<section class="cat" id="drinks" data-cat="Drinks"><h2>Drinks</h2>')
    out.append('<div class="drink-groups">')
    for title, items in DRINKS:
        out.append('<div class="group drink-group">')
        out.append(f"<h3>{e(title)}</h3><ul class=\"drinks\">")
        for n, p in items:
            out.append(
                f'<li class="item"><div class="item-head"><h4>{e(n)}</h4><span class="dots" aria-hidden="true"></span><span class="price">${p}</span></div></li>'
            )
        out.append("</ul></div>")
    out.append("</div></section>")
    return "\n".join(out)


def page(key, title, desc, body, body_class=""):
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if k == key else ""}>{label}</a>'
        for k, href, label in NAV
    )
    footer_links = "".join(f'<li><a href="{href}">{label}</a></li>' for k, href, label in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#7b1426">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;700&family=Young+Serif&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="Bait Sitty, home">
      <img class="brand-logo" src="{LOGO}" alt="" height="48" referrerpolicy="no-referrer" onerror="this.remove()">
      <span class="brand-name">Bait Sitty</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open navigation"><span></span><span></span><span></span></button>
    <nav id="site-nav" class="site-nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="stitch" aria-hidden="true"></div>
  <div class="wrap foot-grid">
    <div>
      <p class="foot-brand">Bait Sitty</p>
      <p class="foot-tag">A taste of home and tradition. The full menu is halal certified.</p>
      <ul class="foot-links">{footer_links}</ul>
    </div>
    <div>
      <h2>Visit</h2>
      <address>{ADDRESS_1}<br>{ADDRESS_2}</address>
      <p><a href="{MAPS_LINK}" target="_blank" rel="noopener">Get directions</a></p>
      <h2>Talk to us</h2>
      <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a><br><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok</a></p>
    </div>
    <div>
      <h2>Hours</h2>
      <table class="hours"><tbody>{hours_rows()}</tbody></table>
    </div>
  </div>
  <p class="wrap legal">© 2026 Bait Sitty Restaurant. Halal certified menu.</p>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
"""


def img(src, alt="", cls="", extra=""):
    return f'<img src="{src}" alt="{e(alt)}" class="{cls}" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display=\'none\'" {extra}>'

# ---------------------------------------------------------------- pages

HOME = f"""
<section class="hero">
  <div class="stitch draw" aria-hidden="true"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="hero-kicker">Mississauga, Ontario</p>
      <h1>Welcome to Bait Sitty</h1>
      <p class="hero-sub">A taste of home and tradition.</p>
      <p class="hero-text">We bring back the warmth and flavors of our grandmothers’ kitchens, where every meal is made with love, patience and authentic homemade recipes. Here, tradition meets comfort, and sharing food means sharing memories, laughter and the true taste of home.</p>
      <div class="btn-row">
        <a class="btn btn-brass" href="menu.html">See the menu</a>
        <a class="btn btn-ghost" href="catering.html">Book an event</a>
      </div>
      <p class="hero-fact">The full menu is halal certified.</p>
    </div>
    <div class="arch-wrap">
      <div class="arch">{img(IMG_ABOUT, "Inside Bait Sitty", "", 'fetchpriority="high"').replace('loading="lazy" ', '')}</div>
    </div>
  </div>
  <div class="stitch draw" aria-hidden="true"></div>
</section>

<section class="section welcome">
  <div class="wrap two">
    <div>
      <p class="pull">Because in our culture, food is love. And at Bait Sitty, love is served generously, just like Sitty always did.</p>
    </div>
    <div class="prose">
      <p>Bait Sitty means grandma’s house. It is where the soulful warmth of home cooking comes to life, where tradition, love and the art of comforting food gather at one table.</p>
      <p>You may arrive as a guest, but you are welcomed as family, just as Sitty welcomed everyone who stepped into her home. There is comfort in every plate, generosity in every serving and love woven into every recipe.</p>
      <p><a class="text-link" href="about.html">Read our story</a></p>
    </div>
  </div>
</section>

<section class="section favourites">
  <div class="wrap">
    <h2 class="section-title">From Sitty’s table</h2>
    <p class="section-lede">A few dishes to start with. Everything is cooked slow, generous and full of soul.</p>
    <ul class="items fav-list">
      {render_item("Ftoor Sitty", "$48", "Qoudsiyeh, foul, falafel, labneh zrar, zait and zaatar, pickles and olives.", "Grandma’s breakfast")}
      {render_item("Hakooret Sitty", "$58", "Hummus, mutabal, muhammarah, labneh harah and a table of Sitty’s salads.", None)}
      {render_item("Dajaj Sitty", "$27", "Fire roasted supreme chicken, taboon bread, sumac, onions and yogurt.", "Musakhan")}
      {render_item("Fattet Hummus", "$16", "Chickpea puree, tahini, yogurt, fried pita, daqa and slivered almonds.", None)}
      {render_item("Cheese and Zaatar Manakeesh", "$8", "Jibneh, nabulsi and Palestinian zaatar spread, freshly baked.", None)}
      {render_item("Kunafeh Nabulsi", "$9", "Sweet, creamy and cheesy, finished with a hint of syrup. Crunchy or soft.", None)}
    </ul>
    <p class="center"><a class="btn btn-red" href="menu.html">Open the full menu</a></p>
  </div>
</section>

<section class="section ambience">
  <div class="wrap two flip">
    <div class="frame">{img(IMG_AMBIENCE, "The dining room at Bait Sitty")}</div>
    <div class="prose">
      <h2>Come sit, savor and make memories</h2>
      <p>Stepping into Bait Sitty feels like walking into your grandmother’s warm embrace. The charm of old world Arab homes meets a refreshed, modern touch: soft earthy tones, warm wood, embroidered details and gentle hints of brass and lace.</p>
      <p class="big">Here, you don’t just dine. You belong.</p>
      <p><a class="text-link" href="gallery.html">See the gallery</a></p>
    </div>
  </div>
</section>

<section class="section events">
  <div class="wrap two">
    <div>
      <h2 class="section-title">Hosting six or more?</h2>
      <p class="section-lede">Family celebrations, private dinners and cultural events feel right at Bait Sitty. Send us your details and we will take care of the rest.</p>
    </div>
    <div class="event-cta">
      <a class="btn btn-red" href="catering.html">Plan your event</a>
      <p>For parties of six or fewer, call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
  </div>
</section>
"""

ABOUT = f"""
<section class="page-head">
  <div class="wrap">
    <h1>About Bait Sitty</h1>
    <p class="lede">A timeless grandmother inspired dining experience.</p>
  </div>
  <div class="stitch" aria-hidden="true"></div>
</section>

<section class="section">
  <div class="wrap two">
    <div class="frame tall">{img(IMG_ABOUT, "Inside Bait Sitty")}</div>
    <div class="prose">
      <p>Bait Sitty is where the soulful warmth of home cooking comes to life. Where tradition, love and the art of comforting food gather at one table. It is a journey back to the flavors of childhood, to the scent of slow cooked meals filling the house and the sound of family gathering before the first bite is served.</p>
      <p>Here, food is more than taste. It is memory, emotion and a story passed down from grandmother’s hands to ours. Bait Sitty nourishes not only the body but the heart, reminding us that the greatest meals were never rushed and the most unforgettable flavors were born in a humble family kitchen.</p>
      <p>At Bait Sitty, you may arrive as a guest, but you are welcomed as family, just as Sitty welcomed everyone who stepped into her home. There is comfort in every plate, generosity in every serving and love woven into every recipe, just as she taught us.</p>
      <p>Inspired by generations of home cooked tradition, our dishes celebrate authenticity, patience and the beauty of simple, honest ingredients. Each plate carries the warmth of grandmother’s touch: a taste of heritage, a whisper of nostalgia and the embrace only home can give.</p>
      <p class="big">Because in our culture, food is love. And at Bait Sitty, love is served generously, just like Sitty always did.</p>
    </div>
  </div>
</section>

<section class="section ambience">
  <div class="wrap two flip">
    <div class="frame">{img(IMG_AMBIENCE, "The dining room at Bait Sitty")}</div>
    <div class="prose">
      <h2>Ambience</h2>
      <p>Stepping into Bait Sitty feels like walking into your grandmother’s warm embrace. A place where time slows down, stories live in every corner and comfort fills the air. The charm of old world Arab homes meets a refreshed, modern touch: soft earthy tones, warm wood, embroidered details and gentle hints of brass and lace that echo memories of family gatherings and lovingly prepared meals.</p>
      <p>Come sit, savor and make memories, just as we always did at Grandma’s house.</p>
      <p class="big">Here, you don’t just dine. You belong.</p>
      <div class="btn-row"><a class="btn btn-brass" href="menu.html">See the menu</a><a class="btn btn-ghost" href="contact.html">Find us</a></div>
    </div>
  </div>
</section>
"""

MENU_PAGE = f"""
<section class="page-head menu-head">
  <div class="wrap two">
    <div>
      <h1>Food and drinks</h1>
      <p class="lede">A new perspective on cherished home traditions.</p>
      <p class="head-text">Every dish tells the story of a loving grandmother’s kitchen, where meals are prepared with patience, pride and a heart full of warmth. Our food is inspired by the comforting flavors we grew up with, crafted just the way grandmother used to make: slow cooked, generous and full of soul.</p>
      <p class="halal">The full menu is halal certified.</p>
    </div>
    <div class="frame">{img(IMG_MENU, "A table of dishes at Bait Sitty")}</div>
  </div>
  <div class="stitch" aria-hidden="true"></div>
</section>

<div class="menu-tools">
  <div class="wrap">
    <label class="search"><span class="sr">Search the menu</span><input id="menu-search" type="search" placeholder="Search the menu, try hummus or lamb" autocomplete="off"></label>
    <nav class="chips" aria-label="Menu categories">
      {"".join(f'<a href="#{c["id"]}">{e(c["label"])}</a>' for c in MENU)}<a href="#drinks">Drinks</a>
    </nav>
  </div>
</div>

<div class="wrap menu-body">
  {render_menu_body()}
  <p class="no-results" hidden>Nothing on the menu matches that search. Try a shorter word, or ask your server.</p>
  <p class="menu-note">Prices are in Canadian dollars. Please tell your server about any allergies.</p>
</div>
"""

gallery_items = "".join(
    f'<li><button type="button" class="g-item" data-full="{BASE}{p}" aria-label="Open photo {i + 1} of {len(GALLERY)}">'
    f'<img src="{BASE}{p}" alt="Bait Sitty photo {i + 1} of {len(GALLERY)}" loading="lazy" referrerpolicy="no-referrer" onerror="this.closest(\'li\').remove()"></button></li>'
    for i, p in enumerate(GALLERY)
)

GALLERY_PAGE = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Gallery</h1>
    <p class="lede">Plates, tables and the room where Sitty’s kitchen lives on.</p>
  </div>
  <div class="stitch" aria-hidden="true"></div>
</section>
<section class="section">
  <div class="wrap">
    <ul class="gallery" id="gallery">{gallery_items}</ul>
  </div>
</section>
<dialog id="lightbox" aria-label="Photo viewer">
  <button type="button" class="lb-close" aria-label="Close">Close</button>
  <button type="button" class="lb-prev" aria-label="Previous photo">Previous</button>
  <img alt="">
  <button type="button" class="lb-next" aria-label="Next photo">Next</button>
</dialog>
"""

CATERING = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Catering and private events</h1>
    <p class="lede">Book an event.</p>
  </div>
  <div class="stitch" aria-hidden="true"></div>
</section>
<section class="section">
  <div class="wrap two form-layout">
    <div class="prose">
      <p>For those who cherish family, food and true hospitality, host your special occasion at Bait Sitty, where every gathering feels like home. Inspired by the warmth of our grandmothers’ kitchens, Bait Sitty brings the comfort of traditional flavors and heartfelt moments to your table.</p>
      <p>Whether it is a family celebration, a private dinner or a cultural event, our cozy and nostalgic atmosphere sets the perfect stage. Enjoy authentic home style dishes, freshly prepared with love, and let us take care of every detail while you focus on your loved ones.</p>
      <p class="note">For parties of six or fewer, please contact our reservations team at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </div>
    <form class="form" data-mailto="{EMAIL}" data-subject="Event enquiry from the Bait Sitty website" novalidate>
      <h2>Tell us about your event</h2>
      <label for="c-name">Your name<input id="c-name" name="name" required autocomplete="name"></label>
      <label for="c-email">Email<input id="c-email" name="email" type="email" required autocomplete="email"></label>
      <label for="c-phone">Phone<input id="c-phone" name="phone" type="tel" autocomplete="tel"></label>
      <div class="row">
        <label for="c-type">Type of event
          <select id="c-type" name="type" required>
            <option value="">Choose one</option>
            <option>Family celebration</option>
            <option>Private dinner</option>
            <option>Cultural event</option>
            <option>Catering</option>
            <option>Something else</option>
          </select>
        </label>
        <label for="c-guests">Number of guests<input id="c-guests" name="guests" type="number" min="6" inputmode="numeric" required></label>
      </div>
      <label for="c-date">Preferred date<input id="c-date" name="date" type="date"></label>
      <label for="c-notes">Anything else we should know<textarea id="c-notes" name="notes" rows="4"></textarea></label>
      <button class="btn btn-red" type="submit">Send event details</button>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
"""

CONTACT = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Contact</h1>
    <p class="lede">Come in, call ahead or send us a note.</p>
  </div>
  <div class="stitch" aria-hidden="true"></div>
</section>
<section class="section">
  <div class="wrap two form-layout">
    <div>
      <div class="contact-block">
        <h2>Bait Sitty</h2>
        <address>{ADDRESS_1}<br>{ADDRESS_2}</address>
        <p><a href="{MAPS_LINK}" target="_blank" rel="noopener">Get directions</a></p>
        <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a><br><a href="{TIKTOK}" target="_blank" rel="noopener">TikTok</a></p>
      </div>
      <div class="contact-block">
        <h2>Hours</h2>
        <table class="hours hours-light"><tbody>{hours_rows()}</tbody></table>
      </div>
    </div>
    <form class="form" data-mailto="{EMAIL}" data-subject="Message from the Bait Sitty website" novalidate>
      <h2>Send a message</h2>
      <label for="m-name">Your name<input id="m-name" name="name" required autocomplete="name"></label>
      <label for="m-email">Email<input id="m-email" name="email" type="email" required autocomplete="email"></label>
      <label for="m-msg">Message<textarea id="m-msg" name="message" rows="5" required></textarea></label>
      <button class="btn btn-red" type="submit">Send message</button>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
<section class="map">
  <iframe title="Map to Bait Sitty, 3145 Dundas St W, Mississauga" src="{MAPS_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</section>
"""

NOT_FOUND = """
<section class="page-head">
  <div class="wrap">
    <h1>That page is not on the menu</h1>
    <p class="lede">The link may be old or mistyped.</p>
    <div class="btn-row"><a class="btn btn-brass" href="index.html">Back to home</a><a class="btn btn-ghost" href="menu.html">See the menu</a></div>
  </div>
  <div class="stitch" aria-hidden="true"></div>
</section>
"""

PAGES = [
    ("index.html", "home", "Bait Sitty Restaurant | A taste of home and tradition", "Grandmother inspired Levantine home cooking in Mississauga. Halal certified menu, brunch, catering and private events.", HOME, "page-home"),
    ("about.html", "about", "About | Bait Sitty Restaurant", "The story and ambience behind Bait Sitty, a grandmother inspired dining experience in Mississauga.", ABOUT, ""),
    ("menu.html", "menu", "Menu | Bait Sitty Restaurant", "Brunch, starters, dips, hot meze, salads, grills, desserts and drinks. The full menu is halal certified.", MENU_PAGE, "page-menu"),
    ("gallery.html", "gallery", "Gallery | Bait Sitty Restaurant", "Photos of the food and the room at Bait Sitty in Mississauga.", GALLERY_PAGE, ""),
    ("catering.html", "catering", "Catering and Private Events | Bait Sitty Restaurant", "Host your family celebration, private dinner or cultural event at Bait Sitty.", CATERING, ""),
    ("contact.html", "contact", "Contact | Bait Sitty Restaurant", "Address, hours, phone and email for Bait Sitty, 3145 Dundas St W, Mississauga.", CONTACT, ""),
    ("404.html", "", "Page not found | Bait Sitty Restaurant", "This page could not be found.", NOT_FOUND, ""),
]

for fname, key, title, desc, body, cls in PAGES:
    write(fname, page(key, title, desc, body, cls))

print("built", len(PAGES), "pages")
