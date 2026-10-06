# Geführte Ersteinrichtung

Führe das Interview in kleinen Etappen mit jeweils ein bis drei Fragen.
Nutze die Frage-/Auswahloberfläche des Hosts, falls verfügbar; sonst normale Chatfragen.
Zeige verständliche Optionen und eine Empfehlung. Antworten im privaten Arbeitsordner
speichern, zunächst mit setup_complete=false. Keine persönlichen Daten aus Beispielen,
anderen Chats oder dem Autor dieses Pakets übernehmen.

## 1. Zweck und Umgebung

Frage: „Soll ich Anzeigen erstellen, Anfragen und Abholungen organisieren oder beides?
Ist dir schnelles Loswerden oder ein guter Erlös wichtiger?“

Kläre Host (Codex / ChatGPT Work lokal / Claude Code), Betriebssystem, lokalen Browser,
Zeitzone und einen eigenen Arbeitsordner für private Verkaufsdaten.
Frage nach der konkreten Verkaufsplattform und ihrer offiziellen URL. Kläre vor
Plattformzugriff, ob die aktuellen Nutzungsbedingungen die gewünschte Automatisierung
erlauben und gegebenenfalls die erforderliche Betreiberzustimmung vorliegt. Bei
Unklarheit nur mit vom Nutzer bereitgestellten Daten Entwürfe erstellen. Weder der
Skill noch ein lokales Profil stellt eine solche Erlaubnis dar. Plattform, Prüfdatum
und erlaubten Umfang minimal in der Konfiguration speichern.

Prüfe verfügbare Browserwerkzeuge nur innerhalb dieser Erlaubnis lesend. Fehlt der Zugriff, leite zur passenden
Einrichtungsanleitung. Behaupte keine erfolgreiche Verbindung, ohne sie getestet zu haben.
Ein manueller Anzeigenassistent ist auch ohne Zeitplanung möglich.

## 2. Häufigkeit und Nutzungsvolumen

Erkläre: Jeder Check verwendet Modell-/Toolkapazität, auch ohne neue Nachrichten.
Lange Verläufe, Bilder und viele einzelne Chats können das weiter erhöhen.
Konkrete Kosten hängen von Tarif und Host ab; keine erfundenen Token- oder Eurobeträge.

Vorschläge:

| Modus | Zeitfenster | Geplante Checks |
| --- | --- | --- |
| Sparsam (Empfehlung) | 09, 12, 15, 18 und 21 Uhr | 5 pro Tag |
| Häufiger | alle 2 Stunden von 09 bis 21 Uhr | 7 pro Tag |
| Manuell | nur auf Auftrag | keine |

Zum Vergleich: alle 20 Minuten von 09 bis 21 Uhr wären 37 Starts.
Diese Zahlen sind Starts, keine garantierten Kostenverhältnisse.
Frage nach Tagen, Uhrzeiten, Zeitzone, Enddatum oder „bis auf Widerruf“.
Erkläre, dass der Rechner während lokaler geplanter Checks eingeschaltet UND wach
sein muss, mit offener Agent-App/CLI-Sitzung und verfügbarem Browser. Zuklappen kann
den Laptop einschlafen lassen. Auf die mitgelieferte macOS-/Windows-Anleitung
verweisen; keine Energie- oder Sperreinstellungen ohne eigenen Auftrag ändern.
Nachts standardmäßig keine Checks. Zeitplan noch nicht aktivieren.

## 3. Abholung und Datenschutz

Erfrage wiederkehrende Verfügbarkeit UND konkrete Ausnahmen, Urlaub und ein
Gültigkeitsdatum. Relative Angaben („morgen“) in lokale ISO-Daten übersetzen und
zur Kontrolle anzeigen. Alte Verfügbarkeit niemals ungeprüft fortschreiben.
Frage nach Versand; vorgeschlagen ist nur Abholung, aber der Nutzer entscheidet.

Frage, welche Ortsangabe öffentlich erscheinen darf und wann eine genaue Adresse
geteilt werden darf. Empfehlung: öffentlich nur die notwendige Orts-/PLZ-Angabe,
genaue Abholadresse erst nach einer vereinbarten Abholung im passenden Chat.
Telefonnummer und besondere Zutrittshinweise nur auf eigene Freigabe teilen.
Genaue Adresse nicht erforderlich, wenn der Nutzer sie selbst übermittelt.

## 4. Autonomie – ausdrückliche Freigaben

Jede dieser Kategorien separat klären und als boolesche Berechtigung speichern:
Nachrichten lesen; Nachrichten senden; Anzeigen veröffentlichen; reservieren;
verkaufte Anzeigen entfernen; Startpreise festlegen; Preise senken;
Gegenangebote annehmen; Bewertungen hinterlassen.
Freigaben gelten nur innerhalb der anschließend vereinbarten Grenzen.

Vorschläge:

- Entwurfsmodus: lesen und Vorschläge erstellen; externe Änderungen erst nach Zustimmung.
- Koordination (Empfehlung): klare Rückfragen und Abholtermine selbst beantworten,
  bestätigte Abholungen reservieren; Veröffentlichung und Preisentscheidungen bestätigen lassen.
- Verkaufsmanagement: zusätzlich Veröffentlichung, Entfernen bestätigter Verkäufe und
  Preiszyklen innerhalb festgelegter Grenzen. Gegenangebote gesondert regeln.

Auch im autonomen Modus bei Widersprüchen, mehreren möglichen Artikeln, unbekannter
Verfügbarkeit, außergewöhnlichen Forderungen oder fehlender Preisgrenze nachfragen.
Die Erlaubnis, Browserwerkzeuge zu benutzen, ist keine pauschale Verkaufsvollmacht.

## 5. Preise, Verhandlungen und Berichte

Frage pro Artikel oder Artikelgruppe nach Ziel (schnell / Erlös), Startpreis,
Untergrenze und erlaubter Senkung. Empfehlung für schnelle Verkäufe: nach zwei
vollen Tagen ohne Anfrage oder Vollpreisinteresse eine moderate Senkung vorschlagen.
Die konkrete Höhe muss genehmigt sein, etwa 10–15 % mit sinnvoller Rundung und
einer expliziten Euro-Untergrenze. Hochwertige Artikel können längere Intervalle haben.
Ohne genehmigten Mechanismus nur Vorschlag, keine automatische Senkung.
Verschenken ist eine eigene Entscheidung, keine implizite Folge eines Preiszyklus.

Bei Gegenangeboten standardmäßig freundlich sagen, dass zunächst auf Interesse zum
ausgeschriebenen Preis gewartet wird und gegebenenfalls eine Rückmeldung folgt.
Annehmen nur bei entsprechender Freigabe und innerhalb des artikelbezogenen Rahmens.

Benachrichtigung wählen: nur Änderungen/Handlungsbedarf (Empfehlung), tägliche
Zusammenfassung oder Übersicht nach jedem Check. Chat ist Standard. Externe
Kanäle benötigen eigene Zustimmung und tatsächlich verfügbare Werkzeuge.

## 6. Login und optionaler Kommunikationsstil

Bei erlaubtem Browsermodus meldet sich der Nutzer selbst auf der gewählten
Verkaufsplattform im lokalen Browser an.
Keine Zugangsdaten abfragen. Mit lesendem Zugriff die Anmeldung überprüfen.

Separat fragen: „Darf ich einige deiner bisherigen eigenen Verkaufsplattform-Nachrichten
lesen, um deinen Schreibstil zu übernehmen? Alternativ nutze ich den freundlichen,
kurzen Standardstil oder Beispiele, die du hier einfügst.“
Ohne Zustimmung keine historischen Chats zur Stilprofilierung lesen.
Mit Zustimmung wenige passende Gespräche (etwa drei bis fünf) auswählen, nur eigene
Formulierungen analysieren. Speichere abstrakte Merkmale, keine Namen, Adressen,
Zitate oder vollständigen Nachrichten fremder Personen als Stilbeispiele.
Die normale Bearbeitung aktueller Verkaufsanfragen benötigt ihre eigene Lesefreigabe.

## 7. Zusammenfassung und Start

Zeige Zweck, Berechtigungen, Preisgrenzen, Verfügbarkeit mit Gültigkeit, Datenschutz,
Stil, Zeitplan und Benachrichtigungen. Bitte einmal um Bestätigung.
Danach setup_complete=true setzen. Zunächst einen manuellen Check durchführen.
Vorhandene Anzeigen gezielt importieren und bestehende Zusagen abgleichen;
keine angenommenen historischen Verkäufe oder Käufer übernehmen.

Zeitplanung nur nach ausdrücklich bestätigtem Auftrag einrichten und den ersten
geplanten Lauf prüfen. Wenn persistente lokale Dateien oder benötigte Werkzeuge
nicht verfügbar sind, die Einschränkung erklären statt zuverlässiges Monitoring zu behaupten.
