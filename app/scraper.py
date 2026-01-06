from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def build_url(item, zip_code):
    return (
        f"https://search.earth911.com/?what={item}"
        f"&where={zip_code}"
        f"&list_filter=all"
        f"&max_distance=25"
    )

def clean_text(s: str):
    if not s:
        return s
    return (
        s.replace('\ufeff', '')
         .replace('\xa0', ' ')
         .replace('\r', ' ')
         .replace('\n', ' ')
         .strip()
    )

def extract_information(url):
    # 1. fetch page
    resp = requests.get(url, verify=False)
    soup = BeautifulSoup(resp.content.decode("utf-8-sig", errors="replace"), "html.parser")

    # 2. find items
    items = soup.find_all("li", class_="result-item")
    items = items[:6]

    facilities = []

    for item in items:
        # title
        title_tag = item.find("h2", class_="title")
        title = clean_text(title_tag.get_text(strip=True)) if title_tag else "No title"

        # phone
        phone_tag = item.find("p", class_="phone")
        phone = clean_text(phone_tag.get_text(strip=True)) if phone_tag else "No phone number listed"

        # address
        contact_ps = item.select(".contact p")
        address_parts = []
        for p in contact_ps:
            text = clean_text(p.get_text(strip=True))
            if not text:
                continue
            # skip phone numbers
            if "(" in text and ")" in text and "-" in text:
                continue
            address_parts.append(text)

        # materials
        material_spans = item.select(".result-materials .matched, .result-materials .material")
        materials = [clean_text(m.get_text(strip=True)) for m in material_spans]
        materials_text = ", ".join(materials) if materials else "No materials listed"

        facility = {
            "Business Name": title,
            "Address": address_parts,
            "Phone": phone,
            "Materials Accepted": materials_text
        }

        facilities.append(facility)

    return facilities
