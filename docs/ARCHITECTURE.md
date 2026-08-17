# um3 architektúra- és függvénytérkép

Tömör, kereshető térkép a kódbázishoz. Célja, hogy egy új feladat előtt gyorsan
eldönthető legyen, melyik fájlban van a releváns logika — nem helyettesíti a
forráskód elolvasását. 

## Belépési pont és adatfolyam

- `main.py:main()` létrehozza a `QApplication`-t, betölti a fordítást
  (`src/messages/hu_HU.qm`), és megnyitja az `ApplicationWindow`-t.
- `ApplicationWindow` a fő hub: minden `action*PushButton` metódusa elrejti
  magát és megnyit egy gyerek `QDialog`-ot (`LocalentryWindow`,
  `EntrypickupWindow`, `ChipControllWindow`, `PreentryWindow`,
  `SendresultWindow`, `SettingsWindow`, `ShowInTheBoxesWindow`). A gyerek
  ablak `closeEvent`-je mindig visszahívja a szülő `.show()`-ját.
- **RFID olvasás adatfolyam:** controller → `Chafonrfid.get_tid()` →
  `chafonrfid.base.CommandRunner` + `ReaderCommand` a soros porton
  (`SerialTransport`) → nyers válasz frame → `uhfreader18.G2InventoryResponseFrame`
  parse → EPC hex string (vagy `None` + `error` string) vissza a controllerhez.
- **Remote adat adatfolyam:** controller → `src/models/*Model` (domain modell)
  → `RemoteApiModel.sendAjaxRequest(link, mode, params)` → HTTP JSON válasz,
  vagy `None` + `self.error`/`self.status_code` beállítás hibán.
- **Két különböző szerver**, ne keverd őket: `SettingsModel.get_server_ip()`
  a timing/timelaps szerver (`/api/entry/...`, `/api/distance/...` stb. JSON
  végpontok, nincs login), `SettingsModel.get_entry_site_url()` a nevezesV2
  regisztrációs oldal (`/api/entry/view-from-startnum` stb., login+CSRF kell).

## Modulok

### `src/controller/` — ablak-vezérlők (`QMainWindow`/`QDialog`)
Egy fájl = egy képernyő. Közös minta: `Ui_*` betöltése `setupUi`-val,
`SettingsModel` az ablak méretezéséhez/maximalizálásához, `closeEvent`
visszaadja a szülő ablakot.

- `WindowMixin` — a controllerek közötti `readRfid`/`resizeText` duplikációt
  kiváltó mixinek, a legtöbb ablak-controller ezt örökli
  - `RfidReaderMixin._readTid(self, comm_port, set_status)` — `Chafonrfid`
    létrehozása, `get_tid()`, hibaüzenet/törlés a megadott `set_status`
    callback-en (pl. `label.setText` vagy `statusbar.showMessage`) keresztül
  - `ResizeFontMixin._resizeFont(self, divisor=40, default_size=14)` — az
    ablak méretezéséhez a betűméretet számoló közös logika
- `ApplicationWindow` — fő hub, megnyitja az almenüket
  - `readRfid(self)` — TID olvasás, vágólapra másolás, hiba a státuszsorba
  - `actionTimesync(self)` — `TimeClient` hívása, szerveridő lekérdezés/szinkron
- `LocalentryWindow` — helyi új nevező felvitele
  - `get_entry_field(self) -> dict` — form mezők → API payload dict
  - `__check_dependies(self) -> bool` — kötelező mezők validálása, piros jelölés
  - `actionSavePushButton(self)` — validál, majd `EntryModel.create_new_entry()`
  - `birthdayChange(self)` — születési dátumból korcsoport auto-kiválasztás
- `EntrypickupWindow` — chip kiadás/visszavétel rajtszám/RFID alapján
  - `actionEntryPickupPushButton` / `actionEntryPickdownPushButton` — RFID
    alapján ki-/bejelölés `EntrypickupModel`-en
  - `fillFields(self, entry: dict)` — nevező adatok kiírása, `pickedUp`
    állapot szerint zöld/piros háttér
- `ChipControllWindow` — időzített (QTimer) chip-kontroll olvasás
  - `scanrfid(self)` — periodikus RFID olvasás + entry lookup, majd a timer
    ideiglenes megállítása `restore_timer`-ig (lásd Buktatók)
- `PreentryWindow` — előnevezés / rajtszám↔RFID párosítás a nevezési oldalon
  - `readStartnum(self, startnum)` — nevező lekérése rajtszám alapján;
    302 státusz = nincs bejelentkezve, 404 = nincs ilyen rajtszám
  - `actionLoginForm(self)` / `try_auto_login(self)` — bejelentkezés nevezesV2-be
  - `actionNextButton` / `actionPrevButton` — rajtszám lépegetés (±1) + olvasás
  - `actionInsertSaveNextpushButton(self)` — RFID beszúrás + mentés + következő
    rajtszám egy gombnyomásra (insert → save → next láncolás)
- `SendresultWindow` — RFID leolvasás időbélyeggel eredményküldéshez
  - `scanrfid(self)` — RFID → `EntrypickupModel.create_entry_timestamp_from_rfid()`
- `SettingsWindow` — `um.conf` szerkesztő UI
  - `collectSettings(self)` / `initValues(self)` — UI ↔ `SettingsModel` szinkron
- `ShowInTheBoxesWindow` — "dobozban" lévő rajtszámok listája/számlálója
  - `actionStartnumLineEditReturnPressed(self)` — kézi rajtszám → `EntryModel.setinthebox`
  - `scanrfid(self)` — RFID alapú dobozba-jelölés, `IntheboxModel.list()` frissít

### `src/models/` — üzleti logika, Qt UI-mentes (kivéve `IntheboxModel`)
- `SettingsModel` — `um.conf` wrapper `ConfigParser`-rel; `get_*`/`set_*`
  getter/setter párok, a setterek `self`-et adnak vissza (fluent), `save_config()`
  írja lemezre
- `RemoteApiModel` — HTTP kliens mindkét szerverhez
  - `sendAjaxRequest(self, link, mode='get', params=None)` — az egyetlen tényleges
    hívó; minden más `get_*_link()`/`get_*_url()` metódus csak URL-t épít
  - `login(self, login: dict) -> bool` — CSRF token scrape (BeautifulSoup) +
    session cookie a nevezesV2 oldalhoz
- `EntryModel` (fájl: `EnrtyModel.py`, elgépelt) — `create_new_entry`,
  `read_entry_from_startnum`, `update_rfid_from_startnum`, `loginSite`,
  `setinthebox` — mind `RemoteApiModel`-re épül
- `EntrypickupModel` — `get_entry_from_rfid`, `updateEntryPickedUp/Down`,
  `create_entry_timestamp_from_rfid`; `checkFormat(entrydatas) -> bool`
  (statikus) ellenőrzi, hogy a válasz tartalmazza-e a várt kulcsokat
- `IntheboxModel(QAbstractTableModel)` — dobozban lévő rajtszámok
  táblázat-modellje (`startnumTableView`-hoz); `list()` tölti újra a szerverről,
  10 oszloponként tördel
- `AgegroupModel` / `DistanceModel` / `GenderModel` — combo-boxokat feltöltő
  referenciaadat modellek; mindhárom szerver-hívással inicializálódik a
  konstruktorban (lásd Buktatók)
- `MyJson.loads(data)` — biztonságos JSON parse, hibán `None`-t ad vissza
  kivétel helyett

### `src/chafonrfid/` — Chafon UHF RFID olvasó driver
- `Chafonrfid.get_tid(self) -> str | None` — magas szintű facade, egyetlen
  TID-et ad vissza (hex, upper); `None` + `self.error`, ha nincs vagy több chip
- `base.ReaderCommand.serialize(self) -> bytearray` — parancsframe checksummal
- `base.CommandRunner.run(self, command)` — parancs küldés + válasz frame olvasás
- `base.ReaderResponseFrame` — nyers byte-okból parse + checksum ellenőrzés
  (`ValueError`-t dob hibás checksumnál)
- `uhfreader18.G2InventoryResponseFrame` — a ténylegesen használt (lásd
  `Chafonrfid.py` importja) válasz-parser
- `uhfreader288m.G2InventoryResponseFrame` — másik reader-modell parsere,
  jelenleg sehol nincs bekötve
- `transport.MockTransport` — teszteléshez, valós soros port nélkül
- `transport_serial.SerialTransport` — a tényleges soros port I/O

### `src/Timesync/` — NTP-szerű óraszinkron kliens/szerver
Saját beágyazott git repóval rendelkezik, lásd Buktatók.
- `TimeClient.run(self)` — csatlakozik a szerverhez, kiszámítja a hálózati
  késleltetést, majd `set_time()`-mal beállítja a helyi órát
- `TimeServer.run(self)` — egyszerű echo-szerver: visszaküldi a saját idejét a
  kliens időbélyegével együtt

## Konvenciók, buktatók

1. **Két különböző szerver** — ne keverd `get_server_ip()` (timing szerver,
   nincs login) és `get_entry_site_url()` (nevezesV2, login+CSRF kell) hívásait.
2. `RemoteApiModel.sendAjaxRequest` a 200/201-en kívül mindent hibaként kezel,
   és `None`-t ad vissza kivétel helyett — hívás után mindig ellenőrizd
   `self.error`-t / `status_code`-ot.
3. `uhfreader18.py` és `uhfreader288m.py` egyaránt `G2InventoryResponseFrame`-et
   definiál, eltérő byte-elrendezéssel; `Chafonrfid.py` jelenleg csak a
   18-as verziót importálja és használja.
4. A generált `Ui_*` fájlokat (`src/views/*/*.py`) soha ne kézzel szerkeszd —
   mindig `pyuic6`-ból generáld újra. A repó
   PyQt6-ra migrált (korábban PyQt5), a `Qt.*`-szerű enumok mind scope-olt
   formában (`Qt.ItemDataRole.DisplayRole` stb.) használandók.
5. `src/Timesync/` saját beágyazott `.git`/`.idea`-t tartalmaz, nem valódi git
   submodule (nincs `.gitmodules`) — a szülő repóban egy blokként jelenik meg
   "modified content"-ként `git status`-ban.
6. `TimeClient.set_time()` `sys.platform` szerint ágazik: Linuxon `sudo date`-et
   hív (jelszó nélküli sudo szükséges hozzá), Windowson egy UAC-jóváhagyást
   kérő emelt jogú PowerShellt indít (`Start-Process -Verb RunAs`) a
   `Set-Date`-hez — nem kell hozzá, hogy az egész alkalmazás eleve
   rendszergazdaként fusson, mindkét irányú parancs `-EncodedCommand`
   base64-kódolással megy át `os.system()`-en az idézőjel-beágyazás elkerülésére.
7. `AgegroupModel`/`DistanceModel`/`GenderModel` a konstruktorban azonnal
   szinkron hálózati hívást indít — ha a szerver nem elérhető, `self.error`-ba
   kerül az üzenet és az `__init__` egyébként nem dob kivételt.
8. `ChipControllWindow.fillFields` a timert leállítja olvasás után és csak
   `get_chipcontroll_wait_after_read()` ms múlva indítja újra
   (`restore_timer`) — ez szándékos "debounce", ne távolítsd el gondolkodás
   nélkül.
9. A mappákban lévő `.pyc` fájlok build/cache artifactok, nem forrás — ne
   ezekből dolgozz, és ne bízz bennük naprakészként.
10. Tesztek a hálózati/soros réteget mockolják (`pytest-mock`,
    `transport.MockTransport`) — új modell/controller teszt írásakor kövesd
    ezt a mintát, ne hívj élő szervert vagy hardvert.
