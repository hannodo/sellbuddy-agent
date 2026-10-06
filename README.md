# SellBuddy

Fotos machen, ein paar Angaben zum Artikel dazuschreiben und den Verkauf organisieren
lassen: SellBuddy hilft dir beim Einstellen von Anzeigen, beantwortet Anfragen und
stimmt Abholtermine ab. Du legst fest, welche Aufgaben der Assistent selbst übernehmen
darf und wann er bei dir nachfragen soll.

SellBuddy ist ein deutschsprachiger Skill für Codex und Claude Code. Nach der
Einrichtung kennt der Assistent deine Abholzeiten, Preisvorstellungen und Wünsche
für die Kommunikation. Eine lokale Übersicht hält fest, welche Artikel noch da
sind und wer sich für wann angekündigt hat.

## Was du brauchst

- Codex / ChatGPT Desktop mit lokalem Browserzugriff oder Claude Code mit
  der Erweiterung „Claude in Chrome“.
- Einen Account auf der Verkaufsplattform, die du verwenden möchtest.
- Einen Rechner mit Internetverbindung, auf dem App und Browser laufen können.

Die Anleitungen führen dich durch das Verbinden des Browsers und die Installation
des Skills. Ob die Browserfunktionen bei dir verfügbar sind, hängt unter anderem
von Tarif, Betriebssystem und App-Version ab. Für den Claude-Code-Weg im Terminal
brauchst du keine Claude-Desktop-App.

Prüfe vor dem Start die Regeln deiner Verkaufsplattform. Automatisierte Zugriffe
können eingeschränkt sein oder eine Zustimmung des Betreibers erfordern. Falls
die Erlaubnis unklar ist, kannst du SellBuddy zunächst für Anzeigen- und
Antwortentwürfe aus deinen eigenen Fotos und Angaben verwenden und die Plattform
selbst bedienen.

## So richtest du es ein

1. Lade das Repository über **Code → Download ZIP** herunter und entpacke es.
   Wenn du Git nutzt, kannst du es auch klonen.
2. Folge der Anleitung für
   [Codex / ChatGPT Desktop](docs/setup-codex.md) oder
   [Claude Code](docs/setup-claude.md). Lege dabei einen eigenen Ordner für deine
   Verkäufe an, zum Beispiel „Meine-Verkaeufe“.
3. Verbinde für den Browsermodus deinen lokalen Browser und melde dich selbst
   auf der Verkaufsplattform an.
4. Starte den Skill mit `$sellbuddy-agent` in Codex oder `/sellbuddy-agent`
   in Claude Code.

Du kannst mit dieser Nachricht beginnen:

> Führe mich durch die Einrichtung von SellBuddy. Ich möchte zuerst festlegen,
> was du für mich übernehmen darfst.

## Deine Regeln für den Verkauf

Der Assistent fragt dich Schritt für Schritt:

- Möchtest du möglichst schnell Platz schaffen oder einen guten Preis erzielen?
- Wann kann jemand etwas abholen? Bietest du auch Versand an?
- Welche Nachrichten darf er selbst beantworten, welche Anzeigen veröffentlichen?
- Darf er Preise senken, und wo liegt deine Untergrenze?
- Wie oft soll er nach neuen Anfragen schauen und dich informieren?

Du bekommst anschließend eine Zusammenfassung zur Bestätigung. Für den ersten
Versuch empfiehlt sich eine Anzeige als Entwurf und ein Nachrichtencheck unter
deiner Aufsicht. So kannst du prüfen, ob alles zu deinen Vorstellungen passt.

Der übliche Ton ist freundlich und kurz. Wenn du möchtest, kann der Assistent
mit deiner Zustimmung einige deiner bisherigen eigenen Nachrichten lesen und
sich an deinem Schreibstil orientieren.

## Im Alltag

Schicke Fotos und eine kurze Beschreibung des nächsten Artikels. Wichtige Angaben
sind Zustand, Größe oder Maße, Zubehör und bekannte Mängel. SellBuddy bereitet
die Anzeige vor und veröffentlicht sie, wenn du das freigegeben hast.

Bei Anfragen orientiert sich der Assistent an deinen Abholzeiten. Sobald eine
Abholung vereinbart ist, kann er den Artikel reservieren und weitere Interessenten
auf die Warteliste setzen. Pro Artikel bleibt es bei einer bestätigten Abholung.
Sag ihm nach der Übergabe kurz Bescheid, damit er die Anzeige und offene Gespräche
abschließen kann.

Kontrolliere gerade am Anfang die Zuordnung der Chats und die zugesagten Termine.
Auch mit einer Verkaufsübersicht kann der Assistent Fehler machen.

## Regelmäßige Checks

Als sparsamen Einstieg empfehlen sich fünf Checks täglich: um 09, 12, 15, 18
und 21 Uhr. Häufigere Checks verbrauchen mehr Nutzungsvolumen, auch wenn niemand
geschrieben hat. Wie viel ein Lauf benötigt, hängt vom Tarif, den Verläufen und
den verwendeten Werkzeugen ab. Häufigkeit und Benachrichtigungen kannst du im
Interview anpassen.

Während der geplanten Checks muss dein Rechner **eingeschaltet und wach** sein.
App und Browser müssen verfügbar bleiben; bei Claude Code im Terminal auch die
Sitzung. Zuklappen, Ruhezustand, ein Neustart oder ein abgelaufener Login können
die Checks unterbrechen.
[So stellst du macOS und Windows dafür ein](docs/keep-awake.md).

Teste den ersten geplanten Lauf. Zum Anhalten genügt der Auftrag:

> Automatisierung pausieren.

Prüfe anschließend, ob der Zeitplan in der App tatsächlich pausiert ist.

## Deine Daten

Die Einstellungen und die Verkaufsübersicht werden in deinem Verkaufsordner
gespeichert. Dieser Ordner kann Käuferdaten und Abholadressen enthalten und sollte
privat bleiben. Wenn du SellBuddy weiterempfiehlst, teile einfach den Link zu diesem
Repository.

Ein eigenes Browserprofil hilft, den Zugriff auf andere Accounts zu begrenzen.
Gib nur die benötigten Browserrechte frei und erledige Login und CAPTCHA selbst.
Passwörter und Cookies gehören weder in den Chat noch in die Verkaufsübersicht.

## Hinweise und Weiterentwicklung

SellBuddy ist ein unabhängiges Projekt. Prüfe die aktuellen Bedingungen deiner
Verkaufsplattform und hole erforderliche Erlaubnisse ein. Das Projekt gibt keine
rechtliche Einschätzung zur Zulässigkeit eines konkreten Einsatzes.

Das Paket steht unter der [MIT-Lizenz](LICENSE). Du kannst es anpassen und
weitergeben. Unter [Datenschutz und Tests](docs/testing.md) findest du die
Testfälle und Hinweise für eigene Änderungen.

GitHub bietet bereits einen
[ZIP-Download der Quelldateien](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).
Für ein separates Offline-Paket gibt es zusätzlich `scripts/build_share.py`;
es nimmt nur die Dateien aus `share-manifest.json` auf.

Stand der Anleitungen: 6. Oktober 2026. Die Offline-Tests wurden ausgeführt;
ein vollständiger Live-Test auf beiden Systemen steht noch aus.
