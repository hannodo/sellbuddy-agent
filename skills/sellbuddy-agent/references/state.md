# Private, persistente Verkaufsübersicht

Arbeite im eigenen Nutzer-Arbeitsordner, nicht im teilbaren Paket:

- .sellbuddy-agent/config.json: Konfiguration und Berechtigungen.
- .sellbuddy-agent/ledger.json: aktuelle Artikel und zugehörige Gespräche.
- .sellbuddy-agent/journal.jsonl: minimale Aktionshistorie.

Vorlagen liegen unter assets. Sie enthalten absichtlich keine aktiven Freigaben.
Private Dateien niemals in ein öffentliches Repository, ZIP oder Skill-Beispiel aufnehmen.
Fotos, Bestellmails, Käufernamen, Adressen, Chats und Browserdaten ebenfalls ausschließen.

## Pro Artikel

Speichere eine stabile lokale ID, Anzeigen-ID und URL, Titel, Zustand/Preis,
Status (draft / available / reserved / sold / removed), Zeitpunkt der
Veröffentlichung und letzten verifizierten Preisänderung, Preisregel und Mindestpreis.
Gespräche enthalten conversation_id, notwendige Anzeigenzuordnung, Kontakt-Anzeigename,
Status (interested / proposed / confirmed / waitlist / declined / completed),
letzte gelesene und zuletzt gesendete Nachricht als ID/Zeitpunkt sowie minimale
Abholvereinbarung mit Datum und Zeitfenster.
Ein confirmed_pickup verweist auf genau EIN Gespräch; interested ist keine Reservierung.
Timestamps mit Zeitzone. Keine vollen Chatkopien, Zugangsdaten oder irrelevanten Kontaktdaten.

## Schreibvorgänge und Wiederaufnahme

1. Aktuelle Dateien lesen. Bei parallel laufendem Check keine externen Änderungen:
   laufenden Check abwarten oder diesen Lauf überspringen.
2. Vor externen Änderungen die beabsichtigte Aktion im Journal als planned notieren.
3. Browseraktion durchführen und ihren sichtbaren Erfolg prüfen.
4. Journalstatus verified oder unknown und Übersicht aktualisieren.

Eine lokale Datei ist keine atomare Transaktion mit einer Webseite. Nach Absturz oder
unklarem Ergebnis zuerst im Browser abgleichen. Nicht einfach planned erneut senden.
Bei fehlenden Gesprächs-IDs nur eine vorläufige Zuordnung verwenden und jede Aktion
über Artikel und vollständigen aktuellen Verlauf verifizieren. Keine Namensgleichheit
als Beweis behandeln.

Die Übersicht unterstützt den Agenten, ersetzt aber nicht den aktuellen Browserzustand.
Bei Widerspruch lesend abgleichen. Unauflösbare Widersprüche dem Nutzer vorlegen.
Keine parallel schreibenden Agenten oder Automationen auf denselben Verkauf ansetzen.
Der Host muss Laufüberschneidungen verhindern; wenn das nicht sichergestellt werden kann,
Monitoring nicht unbeaufsichtigt betreiben.
