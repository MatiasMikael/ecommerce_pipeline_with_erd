# Ecommerce Pipeline with ERD

## Yleiskuvaus
Tämä projekti sisältää ER-diagrammin (Entity-Relationship Diagram), joka kuvaa verkkokaupan tietokannan rakenteen. Diagrammi määrittelee taulut, niiden attribuutit ja relaatioiden väliset yhteydet. Tämä rakenne on keskeinen osa projektin tietokantasuunnittelua.
Tämä projekti on suunniteltu käsittelemään verkkokaupan tietoja relaatiotietokannassa. Projekti seuraa PEP 8 -ohjeistusta koodityylin varmistamiseksi ja keskittyy tietojen hallintaan, analysointiin ja visualisointiin.

Projektin pääpiirteet:
- PostgreSQL-tietokannan käyttö tietojen tallentamiseen ja hallintaan.
- Python-skriptit tiedon generointiin, lataamiseen ja visualisointiin.
- SQLAlchemy ja psycopg2 tietokantayhteyksiin.
- Visualisoinnit luodaan Matplotlibin avulla ja tallennetaan paikallisesti.

## Työkalut ja kirjastot
Tässä projektissa käytetyt työkalut ja kirjastot:

- **Python 3.10**
- **PostgreSQL** (relaatiotietokanta)
- **SQLAlchemy** (tietokantayhteyksien hallintaan)
- **psycopg2** (PostgreSQL-yhteydet)
- **pandas** (datan analysointiin)
- **Matplotlib** (datan visualisointiin)
- **python-decouple** (ympäristömuuttujien hallintaan)
- **ChatGPT** (projektin suunitteluun ja toteutukseen)
  
## Skriptit
Projektin tärkeimmät skriptit ja niiden tarkoitus:

### 1. `generate_data.py`
- Generoi keinotekoista dataa ja tallentaa sen PostgreSQL-tietokantaan.
- Luo seuraavat taulut ja täyttää ne datalla:
  - `asiakkaat`
  - `tilaukset`
  - `tuotteet`
  - `tilauksenrivit`
  - `varasto`

### 2. `create_tables.py`
- Luo tietokannan taulut ERD:n mukaisesti.

### 3. `visualize_data.py`
- Hakee tietoa tietokannasta ja luo seuraavat visualisoinnit:
  - Kuukausittaiset tulot viivakaaviona.
  - Asiakkaiden tilausten määrä histogrammina.
- Tallentaa visualisoinnit kansioon `3_results`.

### 4. `.env`
- Sisältää ympäristömuuttujat, kuten tietokannan nimen, käyttäjän ja salasanan.

## Lopputulos
Projektin lopputuloksena syntyy:
- Hyvin suunniteltu ja dokumentoitu relaatiotietokanta verkkokauppadatan hallintaan.
- Visualisointeja liiketoimintatietojen analysointiin ja ymmärtämiseen.
- PEP 8 -ohjeiden mukainen siisti ja helposti ylläpidettävä koodi.

## Lisenssi
Tämä projekti on lisensoitu **MIT-lisenssillä**. Voit käyttää, muokata ja jakaa projektia vapaasti, kunhan mainitsen alkuperäisen tekijän.
