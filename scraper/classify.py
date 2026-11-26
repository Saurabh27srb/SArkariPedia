"""Domain and name based classification: category and state."""
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# State prefix map — subdomain prefix → state name
# ---------------------------------------------------------------------------
STATE_BY_PREFIX = {
    "up": "Uttar Pradesh",
    "delhi": "Delhi",
    "maharashtra": "Maharashtra",
    "gujaratindia": "Gujarat",
    "gujarat": "Gujarat",
    "tn": "Tamil Nadu",
    "karnataka": "Karnataka",
    "kerala": "Kerala",
    "wb": "West Bengal",
    "rajasthan": "Rajasthan",
    "mp": "Madhya Pradesh",
    "bihar": "Bihar",
    "punjab": "Punjab",
    "haryana": "Haryana",
    "odisha": "Odisha",
    "assam": "Assam",
    "jharkhand": "Jharkhand",
    "uk": "Uttarakhand",
    "uttarakhand": "Uttarakhand",
    "telangana": "Telangana",
    "ap": "Andhra Pradesh",
    "andhra": "Andhra Pradesh",
    "hp": "Himachal Pradesh",
    "himachal": "Himachal Pradesh",
    "goa": "Goa",
    "cg": "Chhattisgarh",
    "chattisgarh": "Chhattisgarh",
    "chhattisgarh": "Chhattisgarh",
    "sikkim": "Sikkim",
    "meghalaya": "Meghalaya",
    "manipur": "Manipur",
    "nagaland": "Nagaland",
    "mizoram": "Mizoram",
    "arunachal": "Arunachal Pradesh",
    "tripura": "Tripura",
    "jammu": "Jammu and Kashmir",
    "jk": "Jammu and Kashmir",
    "ladakh": "Ladakh",
    "chandigarh": "Chandigarh",
    "puducherry": "Puducherry",
    "pondicherry": "Puducherry",
    "andaman": "Andaman and Nicobar Islands",
    "lakshadweep": "Lakshadweep",
    "daman": "Daman and Diu",
    "dnhdd": "Dadra and Nagar Haveli",
}

# ---------------------------------------------------------------------------
# Keyword rules — (category, [keywords])
# More specific first, broader last
# ---------------------------------------------------------------------------
KEYWORDS = [
    # Agriculture
    ("Agriculture", [
        "agri", "kisan", "farmer", "mandi", "enam", "icar", "seednet",
        "soil", "horticulture", "fisheries", "fishery", "animal husbandry",
        "pmfby", "pmkisan", "fasal", "krishi", "dairy", "nafed",
    ]),
    # Health
    ("Health", [
        "health", "mohfw", "nhm", "icmr", "pmjay", "ayush", "aiims", "nhp",
        "cghs", "esi", "esic", "medicalresearch", "vaccine", "covid",
        "nursing", "pharmacy", "dental", "hospital",
    ]),
    # Education
    ("Education", [
        "education", "ugc", "ncert", "cbse", "scholarship", "aicte", "school",
        "university", "college", "naac", "nta", "neet", "jee", "gate",
        "iit", "iisc", "nit", "iim", "kendriya", "navodaya", "eklavya",
        "vidyalaya", "siksha", "shiksha",
    ]),
    # Finance and Tax
    ("Finance and Tax", [
        "finmin", "incometax", "gst", "sebi", "epf", "tax", "cbic",
        "rbi", "nabard", "sidbi", "exim", "customs", "excise",
        "accountant", "cag", "treasury", "finance", "budget",
        "mudra", "pmjdy", "jan dhan", "pension", "nps", "pfrda",
    ]),
    # Law and Justice
    ("Law and Justice", [
        "court", "doj", "legal", "indiacode", "nalsa", "highcourt",
        "supremecourt", "lok adalat", "tribunal", "judiciary", "judge",
        "advocate", "bar council", "prison", "jail", "tihar", "ncrb",
    ]),
    # Defence and Security
    ("Defence and Security", [
        "mod.", "army", "navy", "airforce", "drdo", "police", "mha",
        "bsf", "crpf", "cisf", "itbp", "ssb", "nsg", "nsa", "ra&w",
        "military", "defence", "sainik", "ordnance", "coast guard",
        "territorial army",
    ]),
    # Transport
    ("Transport", [
        "rail", "morth", "parivahan", "civilaviation", "shipping",
        "indianrailways", "irctc", "metro", "nhai", "highway",
        "roadtransport", "dg shipping", "port", "airport", "aviation",
        "inland waterways", "iwai",
    ]),
    # Science and Space
    ("Science and Space", [
        "isro", "dst.", "dbt", "csir", "meity", "iisc",
        "science", "technology", "nuclear", "dae", "atomic",
        "space", "satellite", "nrsc", "sac", "weather", "imd",
        "geological", "survey", "niti", "iiit",
    ]),
    # Environment and Energy
    ("Environment and Energy", [
        "moef", "cpcb", "powermin", "mnre", "jalshakti",
        "environment", "forest", "wildlife", "solar", "wind",
        "petroleum", "coal", "mining", "water", "river", "pollution",
        "ccea", "renewable", "energy", "pcb", "nwda",
    ]),
    # Labour and Jobs
    ("Labour and Jobs", [
        "labour", "ncs.", "eshram", "skill", "employment",
        "rozgar", "job", "naukri", "msme", "startup", "udyam",
        "epfo", "workmen", "dgft", "dipp", "industry",
    ]),
    # Rural and Urban Development
    ("Rural and Urban Development", [
        "rural", "nrega", "mohua", "pmay", "panchayat",
        "urban", "smart city", "swachh", "jnnurm", "amrut",
        "gram", "village", "housing", "slum", "municipal",
        "nulm", "deendayal", "mahatma gandhi",
    ]),
    # Citizen Services
    ("Citizen Services", [
        "uidai", "digilocker", "umang", "passport", "mygov", "rti",
        "pgportal", "serviceonline", "janseva", "citizen", "seva",
        "india.gov", "national portal", "pib", "indiaposts", "post",
        "aadhaar", "darpan", "ekalyan", "samadhan", "grievance",
    ]),
    # Parliament and Elections
    ("Parliament and Elections", [
        "sansad", "eci.", "parliament", "election", "voter",
        "loksabha", "rajyasabha", "assembly", "delimitation",
        "nvsp", "eronet",
    ]),
    # Tourism and Culture
    ("Tourism and Culture", [
        "tourism", "culture", "museum", "heritage", "archaeological",
        "asi.", "incredibleindia", "ttdf", "ngo",
        "yoga", "khelo", "sports", "sai.", "bcci",
    ]),
]

# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def is_official(url: str) -> bool:
    """Return True if the URL belongs to an official Indian government domain."""
    host = urlparse(url).netloc.lower().split(":")[0]
    return (
        host.endswith((".gov.in", ".nic.in", ".gov"))
        or host in ("sansad.in", "india.gov.in")
    )


def normalize(url: str):
    """Return (canonical_url, clean_host) — https, no www, no trailing slash."""
    if "://" not in url:
        url = "https://" + url
    p = urlparse(url)
    host = p.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    # strip port if default
    host = host.split(":")[0]
    canonical = f"https://{host}"
    return canonical, host


def detect_state(host: str):
    """Return state name if the subdomain prefix matches a known state code."""
    parts = host.split(".")
    # pattern: <state>.gov.in  or  <state>.nic.in
    if len(parts) >= 3 and parts[-2] in ("gov", "nic") and parts[-1] == "in":
        prefix = parts[0].lower()
        return STATE_BY_PREFIX.get(prefix)
    return None


def classify(host: str, name: str = ""):
    """Return (category, state_or_None) for a given host + display name."""
    state = detect_state(host)
    if state:
        return "State Governments", state

    text = (host + " " + name).lower()
    for cat, words in KEYWORDS:
        if any(w in text for w in words):
            return cat, None

    return "Other", None
