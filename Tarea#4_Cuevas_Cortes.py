import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def amazon(busqueda, paginas):
    driver = ChromeDriverManager().install()
    s = Service(driver)
    opc = Options()
    opc.add_argument("--start-maximized")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com.mx")
    time.sleep(10)

    txBoxSearch = navegador.find_element(By.ID, "twotabsearchtextbox")
    tnSearch = navegador.find_element(By.ID, "nav-search-submit-button")
    txBoxSearch.send_keys(busqueda)
    time.sleep(5)
    tnSearch.click()
    time.sleep(5)

    productos = []

    for pagina in range(1, paginas + 1):
        time.sleep(5)
        soup = BeautifulSoup(navegador.page_source, "html.parser")

        items = soup.find_all("div", {"data-component-type": "s-search-result"})

        for item in items[:4]:
            nombre_elem = item.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
            if nombre_elem and nombre_elem.find("span"):
                nombre = nombre_elem.find("span").text.strip()
            else:
                nombre = "No disponible"

            precio_elem = item.find("span", class_="a-price-whole")
            if precio_elem:
               precio = precio_elem.text.strip()
            else:
                precio = "No disponible"

            ranking_elem = item.find("span", class_="a-icon-alt")
            if ranking_elem:
                ranking = ranking_elem.text.strip()
            else:
                ranking = "0 Estrellas"

            fecha_entrega_elem = item.find("span", class_="a-color-base a-text-bold")
            if fecha_entrega_elem:
                fecha_entrega = fecha_entrega_elem.text.strip()
            else:
                fecha_entrega = "No disponible"

            productos.append([nombre, precio, ranking, fecha_entrega])

        navegador.save_screenshot(f"imagenes/{busqueda}_{pagina}.png")

        btnNext = navegador.find_elements(By.LINK_TEXT, "Siguiente")
        if btnNext:
            btnNext[0].click()
        else:
            print("No hay más páginas disponibles")
            break

    navegador.quit()

    df = pd.DataFrame(productos, columns=["Nombre", "Precio", "Ranking", "Fecha de Entrega"])
    df.to_csv(f"dataset/{busqueda}_productos.csv")


if __name__ == "__main__":
    busqueda = "Tablets lenovo"
    paginas = 3
    amazon(busqueda, paginas)