from src.crawl.crawl import crawl_url


def test_political_parties():
    url = 'https://tarkvalija.eu/erakondade-sotsiaalpoliitika-lubadused-mis-miks-ja-kuidas/'
    chunks = crawl_url(url)
    expected_chunks = [
        "Eesti 200 lubadus luua inimkeskne abivajaduse hindamise ja pakkumise süsteem on põhjalik ning selgelt argumenteeritud. Probleemikirjeldus ning tänase ja tulevase süsteemi võrdlus on üldiselt arusaadavad. Samas nii uudse ja mahuka ettepaneku toetuseks võiks tuua veelgi selgemaid elulisi kirjeldusi, nt. tuues näiteid “Miks” vastuses viidatud erasektori praktikatest või kirjeldades tulevast paketti ja selle toimimist ühe fiktiivse abivajaja näitel.",
        "Isamaa lubadus meditsiinisüsteemi võimekuse tõstmiseks oli põhjalik ja detailne. Peamised probleemid tulid nii “Mis” kui ka “Miks” vastustes selgelt välja. Samuti sisaldas “Kuidas” vastus mitmeid konkreetseid ettepanekuid nende probleemide lahenduseks. Samas paistis kirjeldusest välja suurem hulk lubadusi, mis olid jaotatud erinevate vastuste alla. See raskendab lubaduste selget eristamist ning nende loogiliste põhjenduste jälgimist. Näiteks paistab lubadus laiendada perearstide vastuvõtuaegasid vastuolus lubadusega leevendada perearstide- ja õdede puudust. Samuti puudub kirjeldus, mis probleemi laupäevane vastuvõtuvõimalus lahendab. Lisaks jääb “Kuidas” vastuses selgusetuks, kuidas kavatsetakse maksumaksjatelt laekuvat raha efektiivsemalt kasutada, mis on nimetatud “nõudlikumad sektorid” ja kuidas suurendatakse erameditsiini panust.",
    ]
    for chunk in expected_chunks:
        assert chunk in chunks


def test_education_fact_sheet():
    url = 'https://tarkvalija.eu/hariduse-faktileht/'
    chunks = crawl_url(url)
    expected_chunks = [
        "*Üldhariduses keskmine õpilaste arv õpetaja kohta: 9,8 (HTM), regionaalselt väga suur kõikumine – mõnes koolis 2 õpilast õpetaja kohta (maakoolid), teises 20+ õpilast õpetaja kohta (Tallinn).",
    ]
    for chunk in expected_chunks:
        assert chunk in chunks
