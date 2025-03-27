import svgwrite

# Fattore di conversione da cm a punti per Illustrator
CM_TO_PT = 28.3465

def genera_layout(espressione, file_output="layout.svg"):
    # Estrai i numeri dalla stringa espressione (es. "24+10x22+6")
    parti = espressione.split("x")  # Separiamo larghezza da altezza
    larghezze = list(map(float, parti[0].split("+")))  # [24, 10]
    altezze = list(map(float, parti[1].split("+")))  # [22, 6]

    # Convertiamo le misure in punti
    larghezza_1 = 3 * CM_TO_PT  # Valore di default
    larghezza_2 = larghezze[0] * CM_TO_PT  # Primo numero
    larghezza_3 = (larghezze[1] / 2) * CM_TO_PT  # Metà del secondo numero

    altezza_centrale = altezze[0] * CM_TO_PT  # Terzo numero
    altezza_superiore = altezze[1] * CM_TO_PT  # Quarto numero
    altezza_inferiore = ((larghezze[1] / 2) + 2) * CM_TO_PT  # Metà del secondo numero + 2

    # Larghezza totale del gruppo
    larghezza_totale = larghezza_1 + (larghezza_2 + larghezza_3 * 2) * 2
    altezza_totale = altezza_superiore + altezza_centrale + altezza_inferiore

    # Creazione file SVG
    dwg = svgwrite.Drawing(file_output, size=(f"{larghezza_totale}pt", f"{altezza_totale}pt"))

    # Posizione iniziale
    x_start = 0
    y_start = altezza_superiore  # Iniziamo sotto il rettangolo superiore

    # Gruppo principale (ripetuto due volte)
    for _ in range(2):
        if x_start == 0:
            dwg.add(dwg.rect(insert=(x_start, y_start), size=(f"{larghezza_1}pt", f"{altezza_centrale}pt"), fill="lightblue"))
            x_start += larghezza_1  

        dwg.add(dwg.rect(insert=(x_start, y_start), size=(f"{larghezza_2}pt", f"{altezza_centrale}pt"), fill="orange"))
        x_start += larghezza_2  

        dwg.add(dwg.rect(insert=(x_start, y_start), size=(f"{larghezza_3}pt", f"{altezza_centrale}pt"), fill="green"))
        x_start += larghezza_3
        dwg.add(dwg.rect(insert=(x_start, y_start), size=(f"{larghezza_3}pt", f"{altezza_centrale}pt"), fill="green"))
        x_start += larghezza_3

    # Rettangolo superiore
    dwg.add(dwg.rect(insert=(0, 0), size=(f"{larghezza_totale}pt", f"{altezza_superiore}pt"), fill="red"))

    # Rettangolo inferiore
    y_bottom = altezza_superiore + altezza_centrale
    dwg.add(dwg.rect(insert=(0, y_bottom), size=(f"{larghezza_totale}pt", f"{altezza_inferiore}pt"), fill="purple"))

    # Salviamo il file
    dwg.save()
    print(f"Layout salvato come {file_output}")

# Esegui il programma con un'espressione
genera_layout("24+10x22+6")
