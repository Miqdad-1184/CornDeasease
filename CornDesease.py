# sistem pakar untuk mengecek penyakit pada jagung
rules = [
    # P001 (Bulai)
    {"if": ["G1", "G2", "G3"], "then": "G4"},
    {"if": ["G3", "G5"], "then": "P001"}, 
    {"if": ["G4"], "then": "G5"},

    # P002 (Blight)
    {"if": ["G5", "G6", "G7"], "then": "G8"},
    {"if": ["G8", "G10"], "then": "P002"},
    {"if": ["G8"], "then": "G9"},
    {"if": ["G5", "G9"], "then": "G10"},

    # P003 (Leaf Rust)
    {"if": ["G10", "G11", "G12"], "then": "G13"},
    {"if": ["G13", "G14"], "then": "P003"},
    {"if": ["G13"], "then": "G14"},

    # P004 (Burn)
    {"if": ["G15", "G16", "G17"], "then": "G18"},
    {"if": ["G18", "G19"], "then": "P004"}, 
    {"if": ["G18"], "then": "G19"},

    # P005 (Stem Borer)
    {"if": ["G20", "G21", "G22"], "then": "G23"},
    {"if": ["G23", "G24"], "then": "G25"},
    {"if": ["G27", "G20", "G23"], "then": "P005"},
    {"if": ["G23"], "then": "G24"},
    {"if": ["G24", "G25"], "then": "G26"},
    {"if": ["G26"], "then": "G27"},

    # P006 (Corn Borer)
    {"if": ["G28", "G29"], "then": "G30"},
    {"if": ["G30"], "then": "G31"},
    {"if": ["G31", "G29"], "then": "P006"}
]

# List semua gejala
symptom_descriptions = {
     "G1": "Chlorotic Colored Leaves: ",
    "G2": "Experiencing growth retardation: ",
    "G3": "The White color is like flour on the upper and lower surfaces of the leaves which are chlorotic: ",
    "G4": "Leaves curled and twisted: ",
    "G5": "Impaired cob formation: ",
    "G6": "Affected leaves look wilted: ",
    "G7": "Several small patches unite to form a larger spot: ",
    "G8": "Elongated light brown patches in the shape of a coil or boat: ",
    "G9": "Brown spots shaped like an elipse: ",
    "G10": "Leaves look dry: ",
    "G11": "Small brown or yellow spots on the leaf surface: ",
    "G12": "Red spots on the midrib: ",
    "G13": "There are irregularly shaped threads that are white and then brown: ",
    "G14": "Comes out powder like yellowfish brown flour: ",
    "G15": "Swelling of the cob: ",
    "G16": "There is a white to black fungus on the seeds: ",
    "G17": "Swollen seeds: ",
    "G18": "Glands are formed in seeds: ",
    "G19": "Kelobot opened and appeared a lot of white to black fungus: ",
    "G20": "There is a small hole in the leaf: ",
    "G21": "Slits in stem: ",
    "G22": "Male flower or cobe base: ",
    "G23": "Stems and tassels (male flowers) that break easily: ",
    "G24": "Stack of broken tassels: ",
    "G25": "Male flowers are not formed: ",
    "G26": "There is flour/dirt around the hoist: ",
    "G27": "Slighly yellow leaves: ",
    "G28": "Transverse holes in the leaf in the vegetative stage: ",
    "G29": "Corncob hair cut/reduced/dry: ",
    "G30": "The tip of the cob has a hoist: ",
    "G31": "Often there are larvae: "
}


facts = []

# kode forward chaining
def forward_chaining(symptoms):
    global facts
    new_fact_added = True
    
    # Tambahkan gejala awal pada fakta yang diketahui
    for symptom in symptoms:
        if symptom not in facts:
            facts.append(symptom)

    while new_fact_added:
        new_fact_added = False
        for rule in rules:
            # Periksa apakah semua ketentuan dalam aturan terpenuhi
            if all(condition in facts for condition in rule["if"]):
                if rule["then"] not in facts:
                    # Tambahkan fakta/gejala yang disimpulkan ke daftar fakta/gejala yang diketahui
                    facts.append(rule["then"])
                    new_fact_added = True
                    print(f"Inferred: {rule['then']}")
    
    # kode untuk mengecek penyakit yang di diagnosis
    diagnoses = []
    if "P001" in facts:
        diagnoses.append("Bulai (P001)")
    if "P002" in facts:
        diagnoses.append("Blight (P002)")
    if "P003" in facts:
        diagnoses.append("Leaf Rust (P003)")
    if "P004" in facts:
        diagnoses.append("Burn (P004)")
    if "P005" in facts:
        diagnoses.append("Stem Borer (P005)")
    if "P006" in facts:
        diagnoses.append("Corn Borer (P006)")
    
    if diagnoses:
        return f"Diagnoses: {', '.join(diagnoses)}"
    else:
        return "No disease diagnosed yet."

#kode untuk menampilkan list gejala
def display_symptoms():
    print("List of all symptoms:")
    for code, description in symptom_descriptions.items():
        print(f"{code}: {description}")

# kode untuk menanyakan dan menerima inputan kode gejala
def ask_symptoms():
    symptoms_input = input("\nMasukkan gejala yang dialami (format: G1-G3-G4): ").strip()
    symptoms = symptoms_input.split("-")
    return symptoms

# Main program
def main():
    global facts
    facts = []  
    print("Sistem pakar penyakit jagung")

    #untuk menampilkan list gejala
    display_symptoms()

    symptoms = ask_symptoms()

   #untuk memanggil kode forward chaining yang sudahh disiapkan
    diagnosis = forward_chaining(symptoms)
    print(diagnosis)

if __name__ == "__main__":
    main()
