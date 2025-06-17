import requests
import xml.etree.ElementTree as ET

URL = "https://urbantv.com.br/epg/00/Otaku.xml"
OUTPUT_FILE = "Otaku_XMLTV.xml"

def format_time(time_str):
    """
    Garante que o tempo esteja no formato XMLTV: YYYYMMDDHHMMSS ±HHMM
    """
    try:
        if ' ' in time_str:
            dt_part, tz_part = time_str.split(" ")
            dt = dt_part.replace("-", "").replace(":", "")
            return f"{dt} {tz_part}"
        else:
            return time_str
    except:
        return "20000101000000 +0000"

def convert_to_xmltv(xml_data):
    root = ET.fromstring(xml_data)
    
    tv = ET.Element("tv", attrib={
        "generator-info-name": "UrbanTV XML Converter",
        "generator-info-url": "https://urbantv.com.br"
    })

    # Adiciona canal (poderíamos carregar mais canais se necessário)
    for ch in root.findall("channel"):
        ch_id = ch.attrib.get("id", "unknown")
        channel_elem = ET.SubElement(tv, "channel", id=ch_id)
        for name in ch.findall("display-name"):
            ET.SubElement(channel_elem, "display-name", name.attrib).text = name.text

    # Adiciona programas
    for prog in root.findall("programme"):
        start = format_time(prog.attrib.get("start", ""))
        stop = format_time(prog.attrib.get("stop", ""))
        channel = prog.attrib.get("channel", "unknown")

        programme = ET.SubElement(tv, "programme", {
            "start": start,
            "stop": stop,
            "channel": channel
        })

        # Campos opcionais
        for child in prog:
            if child.tag in ["title", "desc", "category", "date"]:
                ET.SubElement(programme, child.tag, child.attrib).text = (child.text or "").strip()
            elif child.tag == "credits":
                credits_elem = ET.SubElement(programme, "credits")
                for credit in child:
                    ET.SubElement(credits_elem, credit.tag).text = (credit.text or "").strip()

    return ET.tostring(tv, encoding="utf-8", xml_declaration=True)

def main():
    try:
        print("🔄 Baixando XML da UrbanTV...")
        response = requests.get(URL)
        response.raise_for_status()

        print("✅ Convertendo para XMLTV...")
        xmltv_bytes = convert_to_xmltv(response.content)

        with open(OUTPUT_FILE, "wb") as f:
            f.write(xmltv_bytes)

        print(f"✅ Arquivo XMLTV salvo como: {OUTPUT_FILE}")
    except Exception as e:
        print("❌ Erro durante a conversão:", e)

if __name__ == "__main__":
    main()
